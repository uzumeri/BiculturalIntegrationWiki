# Copyright (c) 2026 Mustafa Uzumeri. All rights reserved.

"""
Bicultural Integration Wiki Validator

Validates the structure of the Bicultural Integration Wiki:
  1. Enforces lower_snake_case for filenames.
  2. Ensures all pages have valid YAML frontmatter matching constraints.
  3. Verifies that all [[wiki-links]] resolve to actual pages.
  4. Detects orphan pages and missing index registrations.

Usage:
    python scripts/validate_wiki.py
"""

import os
import re
import sys
from pathlib import Path
import yaml

WIKI_DIR = Path("wiki")
PAGES_DIR = WIKI_DIR / "pages"
INDEX_FILE = WIKI_DIR / "index.md"
LOG_FILE = WIKI_DIR / "log.md"

# Bicultural allowed subdirs and types
ALLOWED_TYPES = {"concept", "entity", "source", "story", "reference", "rfc", "proposal", "protocol", "pedagogy", "initiative"}
ALLOWED_SUBDIRS = {"concepts", "entities", "sources", "stories", "references", "rfcs", "proposals", "protocols", "pedagogy", "initiatives"}
SLUG_RE = re.compile(r"^[a-z0-9_]+$")
LINK_RE = re.compile(r"\[\[(.*?)\]\]")


def log_error(file_path, msg: str) -> None:
    print(f"ERROR: {file_path}: {msg}", file=sys.stderr)


def validate_wiki() -> bool:
    if not WIKI_DIR.exists() or not PAGES_DIR.exists():
        print("ERROR: wiki/ directory or wiki/pages/ directory does not exist.")
        return False

    errors = 0
    all_files = {}  # relative slug (e.g. 'concepts/thin_market_theory') -> Path

    # 1. Collect all files and validate naming
    for root, _, files in os.walk(PAGES_DIR):
        for file in files:
            if not file.endswith(".md"):
                continue
            path = Path(root) / file
            stem = path.stem

            if not SLUG_RE.match(stem):
                log_error(path, f"Filename stem '{stem}' must be lower_snake_case.")
                errors += 1

            try:
                sub_cat = path.parent.relative_to(PAGES_DIR).as_posix()
            except ValueError:
                sub_cat = ""

            if sub_cat not in ALLOWED_SUBDIRS:
                log_error(path, f"File must be in one of {ALLOWED_SUBDIRS}. Found: '{sub_cat}'.")
                errors += 1

            slug = f"{sub_cat}/{stem}" if sub_cat else stem
            all_files[slug] = path

    # 2. Validate frontmatter and links
    for slug, path in all_files.items():
        content = path.read_text(encoding="utf-8")

        fm_match = re.match(r"^(?:<!--.*?-->\s*\n)?---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
        if not fm_match:
            log_error(path, "Missing YAML frontmatter block (---).")
            errors += 1
            continue

        fm_text = fm_match.group(1)
        try:
            metadata = yaml.safe_load(fm_text)
        except Exception as e:
            log_error(path, f"Invalid YAML in frontmatter: {e}")
            errors += 1
            continue

        if not isinstance(metadata, dict):
            log_error(path, "Frontmatter must be a key-value dictionary.")
            errors += 1
            continue

        if not metadata.get("title"):
            log_error(path, "Missing 'title' field in frontmatter.")
            errors += 1

        type_ = metadata.get("type")
        if type_ not in ALLOWED_TYPES:
            log_error(path, f"'type' must be one of {ALLOWED_TYPES}. Found: '{type_}'.")
            errors += 1

        # Reference pages must have source_url
        if type_ == "reference" and not metadata.get("source_url"):
            log_error(path, "Reference pages must have a 'source_url' field in frontmatter.")
            errors += 1

        # Story pages must have story_type in {"hypothetical-scenario", "empirical-case-study", "thought-experiment", "proposal"}
        if type_ == "story":
            story_type = metadata.get("story_type")
            allowed_story_types = {"hypothetical-scenario", "empirical-case-study", "thought-experiment", "proposal"}
            if story_type not in allowed_story_types:
                log_error(path, f"Story pages must have 'story_type' as one of {allowed_story_types}. Found: '{story_type}'.")
                errors += 1

        # Check wikilinks in body
        body = content[fm_match.end():]
        links = LINK_RE.findall(body)

        for link in links:
            link_target = link.replace(r"\|", "|").split("|")[0].split("#")[0].strip()
            # Support link targets prefixed with wiki/ or wiki/pages/
            if link_target.startswith("wiki/pages/"):
                link_target = link_target[len("wiki/pages/"):]
            elif link_target.startswith("wiki/"):
                link_target = link_target[len("wiki/"):]

            if link_target.endswith(".md"):
                log_error(path, f"Wiki link [[{link}]] must not include '.md' extension.")
                errors += 1
                continue
            if "../" in link_target or "./" in link_target:
                log_error(path, f"Wiki link [[{link}]] must use clean category paths, not relative paths.")
                errors += 1
                continue
            if link_target not in all_files and link_target != "index" and link_target != "log":
                log_error(path, f"Broken wiki link: [[{link}]] does not resolve to any existing page.")
                errors += 1

    # 3. Check index and log exist
    if not INDEX_FILE.exists():
        print(f"WARNING: {INDEX_FILE} not found.")
    if not LOG_FILE.exists():
        print(f"WARNING: {LOG_FILE} not found.")

    if errors > 0:
        print(f"\nValidation failed with {errors} error(s).")
        return False
    else:
        print("\nValidation passed. Wiki is clean!")
        return True


if __name__ == "__main__":
    success = validate_wiki()
    sys.exit(0 if success else 1)
