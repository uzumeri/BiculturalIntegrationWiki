#!/usr/bin/env python3
# Copyright (c) 2026 Mustafa Uzumeri. All rights reserved.

import os
import sys
import subprocess
import tempfile
import re
import base64
import markdown

REPO_ROOT = "/Users/mustafauzumeri/Documents/GitHub/BiculturalIntegrationWiki"
SOP_DIR = os.path.join(REPO_ROOT, "wiki/pages/pedagogy/bicultural_sops")
IMAGES_DIR = os.path.join(REPO_ROOT, "wiki/images")
OUTPUT_PDF = os.path.join(REPO_ROOT, "publications/bicultural_sops_compendium.pdf")

# Define the exact order and categories of the SOPs
SOP_ORDER = [
    # Category 1: Workplace Safety
    ("Workplace Safety Standards", "loto_breaker_isolation.md"),
    ("Workplace Safety Standards", "electrical_panel_access.md"),
    ("Workplace Safety Standards", "confined_space_tank_entry.md"),
    ("Workplace Safety Standards", "working_at_heights_harness.md"),
    ("Workplace Safety Standards", "machine_guarding_interlocks.md"),
    # Category 2: Mechanical & Welding Quality
    ("Mechanical & Welding Quality Standards", "boiler_blowdown_procedure.md"),
    ("Mechanical & Welding Quality Standards", "structural_weld_joint_inspection.md"),
    ("Mechanical & Welding Quality Standards", "heavy_rigging_load_hoist.md"),
    # Category 3: Chemical & Special Processes
    ("Chemical & Special Processes", "chemical_decanting_hazard_label.md"),
    ("Chemical & Special Processes", "liquid_penetrant_inspection.md"),
    ("Chemical & Special Processes", "anodizing_immersion_time.md"),
    ("Chemical & Special Processes", "heat_treating_furnace_log.md"),
    ("Chemical & Special Processes", "composite_layup_hide_tanning.md"),
]

CSS = """
@page {
    size: letter;
    margin: 2.5cm 2.5cm 2.5cm 2.5cm;
}

@page:first {
    margin: 0;
}

body {
    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    font-size: 10.5pt;
    line-height: 1.65;
    color: #1a1a1a;
    max-width: 100%;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
}

/* Cover Page (Light, elegant, print-safe theme) */
.cover-page {
    page-break-after: always;
    padding: 3cm 2cm;
    box-sizing: border-box;
    border: 15px double #1e40af;
    margin: 1.5cm;
    background: #ffffff;
    color: #0f172a;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
}

.cover-title {
    font-size: 28pt;
    font-weight: 800;
    margin-top: 3cm;
    margin-bottom: 20px;
    color: #1e40af; /* Premium blue */
    letter-spacing: -0.02em;
    line-height: 1.2;
}

.cover-subtitle {
    font-size: 16pt;
    font-weight: 400;
    color: #475569;
    margin-bottom: 5cm;
    line-height: 1.4;
    max-width: 90%;
}

.cover-meta {
    font-size: 10.5pt;
    color: #475569;
    margin-top: auto;
    border-top: 1px solid #cbd5e1;
    padding-top: 20px;
    width: 100%;
    margin-bottom: 2cm;
}

.cover-meta p {
    margin: 6px 0;
}

/* Page Break */
.page-break {
    page-break-before: always;
}

/* Section Header Pages (Light, print-safe card layout) */
.section-intro-page {
    page-break-before: always;
    page-break-after: always;
    padding: 6cm 2cm;
    background: #f8fafc; /* Very light slate */
    border-left: 12px solid #1e40af;
    color: #0f172a;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    text-align: left;
    box-sizing: border-box;
}

.section-intro-title {
    font-size: 24pt;
    font-weight: 800;
    color: #1e40af;
    margin-bottom: 20px;
}

.section-intro-desc {
    font-size: 13pt;
    color: #475569;
    max-width: 90%;
    line-height: 1.6;
}

/* Table of Contents */
.toc-page {
    page-break-before: always;
    page-break-after: always;
    padding: 1cm 0;
}

.toc-title {
    font-size: 22pt;
    font-weight: 800;
    color: #0f172a;
    border-bottom: 3px solid #2563eb;
    padding-bottom: 10px;
    margin-bottom: 30px;
}

.toc-section {
    margin-bottom: 25px;
}

.toc-section-title {
    font-size: 14pt;
    font-weight: 700;
    color: #1e40af;
    margin-bottom: 10px;
}

.toc-list {
    list-style: none;
    padding: 0;
    margin: 0;
}

.toc-item {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 8px;
    font-size: 11pt;
}

.toc-item-title {
    color: #334155;
    font-weight: 500;
}

.toc-item-dots {
    flex-grow: 1;
    border-bottom: 1px dotted #cbd5e1;
    margin: 0 10px;
    position: relative;
    top: -4px;
}

.toc-item-page {
    font-weight: 600;
    color: #64748b;
}

/* General Layout styles */
h1 {
    font-size: 24pt;
    font-weight: 800;
    color: #0f172a;
    border-bottom: 3px solid #2563eb;
    padding-bottom: 0.4em;
    margin-top: 0;
    margin-bottom: 0.4em;
    letter-spacing: -0.02em;
}

h2 {
    font-size: 14pt;
    font-weight: 600;
    color: #1e40af;
    margin-top: 1.8em;
    margin-bottom: 0.5em;
    page-break-after: avoid;
}

h3 {
    font-size: 11.5pt;
    font-weight: 600;
    color: #333;
    margin-top: 1.4em;
    margin-bottom: 0.4em;
    page-break-after: avoid;
}

p {
    margin-bottom: 0.7em;
    orphans: 3;
    widows: 3;
}

strong { font-weight: 600; }

blockquote {
    border-left: 3px solid #2563eb;
    margin-left: 0;
    padding: 0.5em 1em;
    background: #f8fafc;
    color: #333;
    font-style: italic;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin: 1em 0;
    font-size: 9.5pt;
    page-break-inside: avoid;
}

th {
    background: #1e40af !important;
    color: white !important;
    font-weight: 600;
    text-align: left;
    padding: 8px 10px;
    font-size: 9pt;
}

td {
    padding: 6px 10px;
    border-bottom: 1px solid #e2e8f0;
    vertical-align: top;
}

tr:nth-child(even) td {
    background: #f8fafc;
}

ul, ol {
    margin-bottom: 0.7em;
    padding-left: 1.5em;
}

li { margin-bottom: 0.3em; }

hr {
    border: none;
    border-top: 1px solid #e2e8f0;
    margin: 1.5em 0;
}

figure.blog-hero {
    margin: 1.5em auto;
    page-break-inside: avoid;
}

img {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 0 auto;
    border-radius: 4px;
}

figcaption {
    font-size: 9pt;
    color: #64748b;
    text-align: center;
    margin-top: 0.6em;
    font-style: italic;
    line-height: 1.4;
}

.intro-section {
    padding: 1cm 0;
}

.intro-section h2 {
    color: #0f172a;
    border-bottom: 2px solid #cbd5e1;
    padding-bottom: 5px;
}
"""

NODE_SCRIPT = """
const puppeteer = require('puppeteer');

(async () => {
    const htmlPath = process.argv[2];
    const pdfPath = process.argv[3];
    const browser = await puppeteer.launch({
        headless: true,
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    });
    const page = await browser.newPage();
    
    // Attach logging handlers
    page.on('console', msg => console.log('PAGE LOG:', msg.text()));
    page.on('pageerror', err => console.log('PAGE ERROR:', err.toString()));
    page.on('requestfailed', request => console.log('REQUEST FAILED:', request.url(), request.failure().errorText));

    await page.goto('file://' + htmlPath, { waitUntil: 'networkidle0' });

    // Wait 8 seconds to allow the browser to fully parse, load, and decode all Base64 images
    await new Promise(resolve => setTimeout(resolve, 8000));

    const headerTemplate = `<div style="width:100%; margin: 0 auto; padding: 0 2.5cm; font-size:9px; color:#334155; font-family:\\'Helvetica Neue\\',Helvetica,Arial,sans-serif; display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #cbd5e1; padding-bottom:5px; -webkit-print-color-adjust:exact; print-color-adjust:exact;"><span style="font-weight:800; color:#1e40af; text-transform:uppercase; letter-spacing:0.06em;">Bicultural Integration Wiki</span><span style="font-weight:500; color:#475569;">Dual-Register SOP Compendium</span></div>`;
    
    const footerTemplate = `<div style="width:100%; margin: 0 auto; padding: 0 2.5cm; font-size:8px; color:#334155; font-family:\\'Helvetica Neue\\',Helvetica,Arial,sans-serif; display:flex; justify-content:space-between; align-items:center; border-top:1px solid #cbd5e1; padding-top:5px; -webkit-print-color-adjust:exact; print-color-adjust:exact;"><span style="font-weight:600;">© 2026 Mustafa Uzumeri. All rights reserved.</span><span style="font-style:italic; font-size:7.5px; color:#475569;">Bicultural Integration Exchange Project</span><span style="font-weight:600;">Page <span class="pageNumber"></span> of <span class="totalPages"></span></span></div>`;

    await page.pdf({
        path: pdfPath,
        format: 'Letter',
        printBackground: true,
        displayHeaderFooter: true,
        headerTemplate: headerTemplate,
        footerTemplate: footerTemplate,
        margin: {
            top: '2.4cm',
            bottom: '2.4cm',
            left: '2.5cm',
            right: '2.5cm'
        }
    });
    await browser.close();
    console.log("PDF generated successfully.");
})();
"""

def parse_frontmatter(content):
    lines = content.split('\n')
    metadata = {}
    i = 0
    
    if lines and lines[0].startswith('<!--'):
        while i < len(lines) and '-->' not in lines[i]:
            i += 1
        i += 1
        
    while i < len(lines) and lines[i].strip() == '':
        i += 1
        
    if i < len(lines) and lines[i].strip() == '---':
        i += 1
        frontmatter_lines = []
        while i < len(lines) and lines[i].strip() != '---':
            frontmatter_lines.append(lines[i])
            i += 1
        if i < len(lines):
            i += 1
            
        for line in frontmatter_lines:
            if ':' in line:
                key, val = line.split(':', 1)
                key = key.strip()
                val = val.strip()
                if val.startswith('"') and val.endswith('"'):
                    val = val[1:-1]
                elif val.startswith("'") and val.endswith("'"):
                    val = val[1:-1]
                metadata[key] = val
                
    clean_content = '\n'.join(lines[i:])
    return metadata, clean_content

def embed_images_as_base64(html_content):
    """Finds image tags and replaces their source with base64 encoded data URIs."""
    def replace_img_path(match):
        img_filename = match.group(1)
        abs_img_path = os.path.abspath(os.path.join(IMAGES_DIR, img_filename))
        if os.path.exists(abs_img_path):
            with open(abs_img_path, "rb") as img_file:
                data = img_file.read()
                # Determine mime type by magic bytes
                mime_type = "image/png"
                if data.startswith(b"\xff\xd8"):
                    mime_type = "image/jpeg"
                elif data.startswith(b"\x89PNG"):
                    mime_type = "image/png"
                elif data.startswith(b"GIF8"):
                    mime_type = "image/gif"
                encoded = base64.b64encode(data).decode('utf-8')
                print(f"  Embedded visual asset: {img_filename} (detected mime: {mime_type})")
                return f'src="data:{mime_type};base64,{encoded}"'
        else:
            print(f"  WARNING: Visual asset not found: {abs_img_path}")
            return match.group(0)
    
    # Matches src="../../../images/filename.png" or src="../../images/filename.png" etc.
    return re.sub(r'src="(?:\.\./)+images/(.+?)"', replace_img_path, html_content)

def build_compendium_html():
    html_sections = []
    
    # 1. Add Cover Page
    cover_html = """
    <div class="cover-page">
        <div class="cover-title">BICULTURAL STANDARD OPERATING PROCEDURES</div>
        <div class="cover-subtitle">A Dual-Register Compendium for Canadian High-Stakes Manufacturing</div>
        <div class="cover-meta">
            <p><strong>Published:</strong> June 2026</p>
            <p><strong>Project:</strong> Bicultural Integration Exchange</p>
            <p><strong>Lineage & Pedagogy:</strong> Dr. Linda Manyguns (MRU) & Mustafa Uzumeri</p>
            <p>© 2026 Mustafa Uzumeri. All rights reserved.</p>
        </div>
    </div>
    """
    html_sections.append(cover_html)
    
    # 2. Add Introduction Page
    intro_html = """
    <div class="intro-section page-break">
        <h1>Introduction: The Dual-Register Playbook</h1>
        <p>This compendium compiles thirteen bicultural, dual-register Standard Operating Procedures (SOPs) developed for the Canadian high-stakes manufacturing and aerospace industries. In industrial settings, safety and quality compliance are governed by rigid, non-negotiable standards (such as CSA codes and Nadcap requirements). However, traditional settler-style onboarding often relies on expository, text-dense manuals that fail to engage or respect the oral, relational pedagogy of Indigenous communities.</p>
        <p>The <strong>Dual-Register Playbook</strong> bridges this gap by presenting every procedure in two distinct but parallel registers:</p>
        <ul>
            <li><strong>Register A (Conventional Expository SOP)</strong>: The standard, formal, technical procedure required for quality management system audits, outlining exact sizes, angles, tolerances, and compliance warnings.</li>
            <li><strong>Register B (Bicultural Relational Narrative)</strong>: A narrative translation of the same process that explains the <em>why</em> of the rules using traditional metaphors (such as raw-hide lashings, bow wood curing, and the natural warning signs of animals). This register shifts motivation from external audit fear to internal values-based care and community protection.</li>
        </ul>
        <h2>Pedagogical Background & Lineage</h2>
        <p>This work is built on two primary foundations:</p>
        <ol>
            <li><strong>Mustafa Uzumeri's ISO 9001 Research</strong>: Academic and practical investigations into quality standardization and empirical training systems (iPOV), mapping how process verification can be made intuitive without reducing rigor.</li>
            <li><strong>Dr. Linda Manyguns' Storytelling Pedagogy</strong>: Collaborative frameworks centering North American Indigenous verb-centered grammars, relation-first causation models, and oral storytelling as the primary vehicle for legal and operational norms. A notable example is her large-scale hide-tanning workshop, which serves as the direct metaphor for aerospace composite layup and autoclave curing.</li>
        </ol>
        <p>By pairing these registers, this compendium ensures that shop floor operators achieve full technical proficiency while maintaining deep alignment with their cultural identity and community values.</p>
    </div>
    """
    html_sections.append(intro_html)
    
    # 3. Add Table of Contents
    toc_html = """
    <div class="toc-page page-break">
        <div class="toc-title">Table of Contents</div>
        
        <div class="toc-section">
            <div class="toc-section-title">Workplace Safety Standards (CSA Group)</div>
            <ul class="toc-list">
                <li class="toc-item"><span class="toc-item-title">SOP 1: LOTO Breaker Isolation (CSA Z460)</span><span class="toc-item-dots"></span><span class="toc-item-page">Page 6</span></li>
                <li class="toc-item"><span class="toc-item-title">SOP 2: Electrical Panel Access (CSA Z462)</span><span class="toc-item-dots"></span><span class="toc-item-page">Page 12</span></li>
                <li class="toc-item"><span class="toc-item-title">SOP 3: Confined Space Tank Entry (CSA Z1006)</span><span class="toc-item-dots"></span><span class="toc-item-page">Page 18</span></li>
                <li class="toc-item"><span class="toc-item-title">SOP 4: Working at Heights Harness (CSA Z259)</span><span class="toc-item-dots"></span><span class="toc-item-page">Page 24</span></li>
                <li class="toc-item"><span class="toc-item-title">SOP 5: Machine Guarding Interlocks (CSA Z432)</span><span class="toc-item-dots"></span><span class="toc-item-page">Page 29</span></li>
            </ul>
        </div>
        
        <div class="toc-section">
            <div class="toc-section-title">Mechanical & Welding Quality Standards (CSA Group / CWB)</div>
            <ul class="toc-list">
                <li class="toc-item"><span class="toc-item-title">SOP 6: Boiler Blowdown Procedure (CSA B51)</span><span class="toc-item-dots"></span><span class="toc-item-page">Page 35</span></li>
                <li class="toc-item"><span class="toc-item-title">SOP 7: Structural Weld Joint Inspection (CSA W178.2)</span><span class="toc-item-dots"></span><span class="toc-item-page">Page 40</span></li>
                <li class="toc-item"><span class="toc-item-title">SOP 8: Heavy Rigging Load Hoist (CSA Z150)</span><span class="toc-item-dots"></span><span class="toc-item-page">Page 45</span></li>
            </ul>
        </div>
        
        <div class="toc-section">
            <div class="toc-section-title">Chemical & Aerospace Special Processes (WHMIS / Nadcap)</div>
            <ul class="toc-list">
                <li class="toc-item"><span class="toc-item-title">SOP 9: Chemical Decanting Hazard Label (WHMIS 2015)</span><span class="toc-item-dots"></span><span class="toc-item-page">Page 52</span></li>
                <li class="toc-item"><span class="toc-item-title">SOP 10: Liquid Penetrant Inspection (Nadcap AC7114)</span><span class="toc-item-dots"></span><span class="toc-item-page">Page 57</span></li>
                <li class="toc-item"><span class="toc-item-title">SOP 11: Aluminum Anodizing (Nadcap AC7108)</span><span class="toc-item-dots"></span><span class="toc-item-page">Page 62</span></li>
                <li class="toc-item"><span class="toc-item-title">SOP 12: Heat Treating Furnace Log (Nadcap AC7102)</span><span class="toc-item-dots"></span><span class="toc-item-page">Page 68</span></li>
                <li class="toc-item"><span class="toc-item-title">SOP 13: Composite Layup & Curing (Nadcap AC7118)</span><span class="toc-item-dots"></span><span class="toc-item-page">Page 74</span></li>
            </ul>
        </div>
    </div>
    """
    html_sections.append(toc_html)
    
    current_category = None
    
    # 4. Add each SOP file
    for category, filename in SOP_ORDER:
        file_path = os.path.join(SOP_DIR, filename)
        if not os.path.exists(file_path):
            print(f"ERROR: SOP file {filename} not found.")
            continue
            
        # Add a Section divider page if the category changes
        if category != current_category:
            current_category = category
            section_desc = ""
            if category == "Workplace Safety Standards":
                section_desc = "SOPs governing personal protection, mechanical isolation, and boundary protection under CSA Group safety regulations."
            elif category == "Mechanical & Welding Quality Standards":
                section_desc = "SOPs governing high-pressure vessels, structural welding integrity, and heavy rigging operations under CSA and CWB codes."
            elif category == "Chemical & Special Processes":
                section_desc = "SOPs governing chemical processing, non-destructive testing (NDT), heat treating, and composite autoclave curing under WHMIS and Nadcap standards."
                
            sec_html = f"""
            <div class="section-intro-page">
                <div class="section-intro-title">{category}</div>
                <div class="section-intro-desc">{section_desc}</div>
            </div>
            """
            html_sections.append(sec_html)
            
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        metadata, content = parse_frontmatter(content)
        
        # Convert markdown body to HTML
        html_body = markdown.markdown(
            content,
            extensions=['tables', 'smarty', 'sane_lists'],
            output_format='html5'
        )
        
        # Embed the local images as base64 URIs into the HTML body
        html_body = embed_images_as_base64(html_body)
        
        # Replace loading="lazy" with loading="eager" to ensure headless Chrome renders all images
        html_body = html_body.replace('loading="lazy"', 'loading="eager"')
        
        # Wrap each SOP in a page-break div
        sop_html = f"""
        <div class="sop-container page-break">
            {html_body}
        </div>
        """
        html_sections.append(sop_html)
        
    full_html = f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Bicultural Standard Operating Procedures Compendium</title>
        <style>{CSS}</style>
    </head>
    <body>
        {''.join(html_sections)}
    </body>
    </html>
    """
    return full_html

def generate_pdf():
    # Make sure output directory exists
    os.makedirs(os.path.dirname(OUTPUT_PDF), exist_ok=True)
    
    # 1. Build the unified HTML string
    print("Building unified compendium HTML with base64 embedded visual assets...")
    compendium_html = build_compendium_html()
    
    # 2. Write HTML to scratch directory
    html_path = os.path.join(REPO_ROOT, "scratch/compendium.html")
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(compendium_html)
        
    # Write the Node print script to a temp file
    temp_dir = tempfile.gettempdir()
    js_path = os.path.join(temp_dir, "print_compendium.js")
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(NODE_SCRIPT)
        
    print(f"HTML written to {html_path}")
    
    # 3. Ensure puppeteer is installed in the temp directory
    print("Installing Puppeteer in temp directory...")
    subprocess.run(
        ['npm', 'install', 'puppeteer'],
        cwd=temp_dir,
        capture_output=True,
        timeout=120
    )
    
    # 4. Execute Puppeteer rendering
    print("Rendering PDF via Puppeteer...")
    result = subprocess.run(
        ['node', js_path, html_path, OUTPUT_PDF],
        cwd=temp_dir,
        capture_output=True,
        text=True,
        timeout=60
    )
    
    if result.returncode != 0:
        print(f"Error executing Puppeteer: {result.stderr}", file=sys.stderr)
        sys.exit(1)
        
    print(f"PDF generated successfully at {OUTPUT_PDF}")
    
    # Clean up temp JS file only
    try:
        os.unlink(js_path)
    except OSError:
        pass

if __name__ == '__main__':
    generate_pdf()
