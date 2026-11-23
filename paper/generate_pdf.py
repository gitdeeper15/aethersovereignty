#!/usr/bin/env python3
"""
Generate PDF from AetherSovereignty Markdown paper using pandoc + weasyprint.
"""

import subprocess
import sys
from pathlib import Path

BASE = Path("/storage/emulated/0/Download/AetherSovereignty/paper")
MD = BASE / "AetherSovereignty_Research_Paper_v1.0.0.md"
HTML = BASE / "AetherSovereignty_Research_Paper_v1.0.0.html"
PDF = BASE / "AetherSovereignty_Research_Paper_v1.0.0.pdf"
CSS = BASE / "style.css"

if not MD.exists():
    print(f"ERROR: {MD} not found")
    sys.exit(1)

# Step 1: Markdown -> HTML via pandoc
print("[1/2] Converting Markdown -> HTML via pandoc...")
cmd = [
    "pandoc", str(MD),
    "-o", str(HTML),
    "--standalone",
    "--toc",
    "--toc-depth=2",
    "--number-sections",
    "--metadata", "title=AetherSovereignty: The Architectural Independence of Sovereignty in Autonomous Agent Systems",
    "--metadata", "author=Samir Baladi",
    "--metadata", "lang=en",
    "--css", "style.css",
]
result = subprocess.run(cmd, capture_output=True, text=True)
if result.returncode != 0:
    print("PANDOC FAILED:")
    print(result.stderr)
    sys.exit(1)
print(f"    OK: {HTML}")

# Step 2: HTML -> PDF via weasyprint
print("[2/2] Converting HTML -> PDF via weasyprint...")
try:
    from weasyprint import HTML as WHTML, CSS as WCSS
    WHTML(filename=str(HTML), base_url=str(BASE)).write_pdf(str(PDF))
except Exception as e:
    print(f"WEASYPRINT FAILED: {e}")
    sys.exit(1)

if PDF.exists():
    size_kb = PDF.stat().st_size // 1024
    print(f"    OK: {PDF} ({size_kb} KB)")
else:
    print("ERROR: PDF not created")
    sys.exit(1)
