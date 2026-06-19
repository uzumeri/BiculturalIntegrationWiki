# Copyright (c) 2026 Mustafa Uzumeri. All rights reserved.
"""
sync_sources.py
Pulls source documents from DeeperPoint ecosystem repos into sources/
according to sync_manifest.yaml. Uses local workspace first, then falls back
to GitHub REST API with GITHUB_PAT if not found.

Usage:
    python scripts/sync_sources.py [--dry-run] [--force]

Options:
    --dry-run   Report what would be pulled without writing files.
    --force     Pull all ingest-class files regardless of SHA change.
                By default, pinned files are skipped unless --force is set.

Exit codes:
    0  — Clean run, no changes needed (or dry-run complete).
    1  — One or more files changed; callers should trigger /wiki-ingest.
    2  — Error (API failure, missing token, etc.)
"""

import os
import sys
import json
import base64
import argparse
from pathlib import Path

import httpx
import yaml
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).parent.parent.resolve()
MANIFEST_FILE = BASE_DIR / "sync_manifest.yaml"
SOURCES_DIR = BASE_DIR / "sources"
SHA_CACHE_FILE = BASE_DIR / "sources" / ".sha_cache.json"

GITHUB_PAT = os.getenv("GITHUB_PAT", "")
GITHUB_API = "https://api.github.com"


def load_manifest() -> list[dict]:
    """Load and return the list of source entries from sync_manifest.yaml."""
    with open(MANIFEST_FILE, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data.get("sources", [])


def load_sha_cache() -> dict:
    """Load the last-seen SHA cache. Returns empty dict if not found."""
    if SHA_CACHE_FILE.exists():
        with open(SHA_CACHE_FILE, encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_sha_cache(cache: dict) -> None:
    """Persist the SHA cache to disk."""
    SOURCES_DIR.mkdir(parents=True, exist_ok=True)
    with open(SHA_CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=2)


def github_get_file(repo: str, filepath: str, branch: str = "main") -> dict:
    """
    Fetch file metadata and content from GitHub REST API.
    Returns dict with 'sha', 'content' (decoded str), 'size'.
    Raises RuntimeError on API errors.
    """
    url = f"{GITHUB_API}/repos/{repo}/contents/{filepath}?ref={branch}"
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if GITHUB_PAT:
        headers["Authorization"] = f"Bearer {GITHUB_PAT}"

    with httpx.Client(timeout=30, follow_redirects=True) as client:
        r = client.get(url, headers=headers)

    if r.status_code == 404:
        raise RuntimeError(f"File not found in {repo}: {filepath} (branch: {branch})")
    if r.status_code == 403:
        raise RuntimeError(f"GitHub API rate limit or permission error for {repo}/{filepath}.")
    if r.status_code != 200:
        raise RuntimeError(f"GitHub API error {r.status_code} for {repo}/{filepath}: {r.text[:200]}")

    data = r.json()
    if data.get("encoding") == "base64":
        content = base64.b64decode(data["content"]).decode("utf-8", errors="replace")
    else:
        content = data.get("content", "")

    return {
        "sha": data["sha"],
        "content": content,
        "size": data.get("size", 0),
    }


def sync_sources(dry_run: bool = False, force: bool = False) -> int:
    """
    Main sync loop. Returns exit code: 0 = no changes, 1 = changes found.
    """
    if not GITHUB_PAT:
        print("WARNING: GITHUB_PAT not set. API calls will be rate-limited.", file=sys.stderr)

    sources = load_manifest()
    sha_cache = load_sha_cache()
    changed: list[str] = []
    errors: list[str] = []

    SOURCES_DIR.mkdir(parents=True, exist_ok=True)

    for entry in sources:
        repo = entry.get("repo", "")
        filepath = entry.get("file", "")
        branch = entry.get("branch", "main")
        target = entry.get("target")
        classification = entry.get("classification", "ingest")
        pinned = entry.get("pin") == "stable"

        cache_key = f"{repo}/{filepath}"

        # Skip reference-class files — we don't pull content for those
        if classification == "reference" or not target or target == "~":
            print(f"  SKIP (reference): {repo}/{filepath}")
            continue

        # Skip pinned files unless forced
        if pinned and not force:
            print(f"  SKIP (pinned, use --force to update): {repo}/{filepath}")
            continue

        # Try local path lookup first
        import platform
        is_windows = platform.system() == "Windows"
        
        if is_windows:
            base_dir = r"C:\Users\MustafaUzumeri\GitHub"
        else:
            base_dir = "/Users/mustafauzumeri/Documents/GitHub"

        LOCAL_REPO_MAP = {
            "DeeperPoint/TeardownWorkbench": f"{base_dir}/TeardownWorkbench",
            "DeeperPoint/Cosolvent": f"{base_dir}/Cosolvent",
            "DeeperPoint/ClientSynth": f"{base_dir}/ClientSynth",
            "DeeperPoint/KnowledgeSlot": f"{base_dir}/CommonContext",
            "DeeperPoint/DeeperpointBusiness": f"{base_dir}/DeeperpointBusiness",
            "DeeperPoint/MarketForge": f"{base_dir}/MarketForge",
            "DeeperPoint/DeeperPointBlogging": f"{base_dir}/DeeperPointBlogging",
            "DeeperPoint/deeperpoint.github.io": f"{base_dir}/deeperpoint.github.io",
        }
        local_base = LOCAL_REPO_MAP.get(repo)
        local_file = Path(local_base) / filepath if local_base else None
        if local_file and local_file.exists():
            print(f"    [LOCAL] Found locally: {local_file}")
            try:
                content = local_file.read_text(encoding="utf-8")
                import hashlib
                sha = hashlib.sha1(f"blob {len(content.encode('utf-8'))}\0".encode("utf-8") + content.encode("utf-8")).hexdigest()
                result = {
                    "sha": sha,
                    "content": content,
                    "size": len(content.encode("utf-8"))
                }
            except Exception as exc:
                print(f"    [LOCAL ERROR] Failed to read local file: {exc}", file=sys.stderr)
                local_file = None
        else:
            local_file = None

        if not local_file:
            try:
                result = github_get_file(repo, filepath, branch)
            except RuntimeError as exc:
                print(f"  ERROR: {exc}", file=sys.stderr)
                errors.append(cache_key)
                continue

        current_sha = result["sha"]
        cached_sha = sha_cache.get(cache_key)

        if current_sha == cached_sha and not force:
            print(f"    [OK] Up to date (SHA: {current_sha[:8]})")
            continue

        # File has changed (or is being force-pulled)
        status = "CHANGED" if cached_sha else "NEW"
        print(f"    [{status}] (was: {str(cached_sha)[:8] if cached_sha else 'none'}, now: {current_sha[:8]}, {result['size']} bytes)")

        if not dry_run:
            target_path = BASE_DIR / target
            target_path.parent.mkdir(parents=True, exist_ok=True)
            target_path.write_text(result["content"], encoding="utf-8")
            sha_cache[cache_key] = current_sha
            print(f"    [WRITTEN] {target}")
        else:
            print(f"    (dry-run) Would write to {target}")

        changed.append(cache_key)

    if not dry_run:
        save_sha_cache(sha_cache)

    print()
    if errors:
        print(f"Sync completed with {len(errors)} error(s): {errors}", file=sys.stderr)

    if changed:
        print(f"Changed files ({len(changed)}) -- run /wiki-ingest on each:")
        for c in changed:
            print(f"  {c}")
        return 1

    print("All sources up to date. No wiki-ingest needed.")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sync BiculturalIntegrationWiki source docs into sources/")
    parser.add_argument("--dry-run", action="store_true", help="Report changes without writing files")
    parser.add_argument("--force", action="store_true", help="Pull all files regardless of SHA")
    args = parser.parse_args()

    exit_code = sync_sources(dry_run=args.dry_run, force=args.force)
    sys.exit(exit_code)
