#!/usr/bin/env python3
"""Insert figure references into the paper at specified anchor points."""

from pathlib import Path

MD = Path("/storage/emulated/0/Download/AetherSovereignty/paper/AetherSovereignty_Research_Paper_v1.0.0.md")
text = MD.read_text(encoding="utf-8")

FIG_DIR = "../docs/figure"

insertions = [
    # (anchor line substring, figure markdown block, position: 'after' or 'before')
    (
        "### 3.1 Origin of the concept",
        f"\n![Figure 2: Conceptual Genesis and Methodological Reconstruction]({FIG_DIR}/Fig2_Conceptual_Genesis.png)\n",
        "after",
    ),
    (
        "### 4.1 The foundational dimensions",
        f"\n![Figure 1: The Aether Family — Eleven Dimensions and Candidates]({FIG_DIR}/Fig1_Eleven_Dimensions.png)\n",
        "after",
    ),
    (
        "### 5.1 Bracketing, not replacement",
        f"\n![Figure 4: Bracketing vs. Replacement]({FIG_DIR}/Fig4_Bracketing.png)\n",
        "after",
    ),
    (
        "### 6.1 The four levels",
        f"\n![Figure 3: Four-Level Functional Stratification]({FIG_DIR}/Fig3_Four_Levels.png)\n",
        "after",
    ),
    (
        "### 7.1 Two competing hypotheses",
        f"\n![Figure 5: The Testing Dichotomy]({FIG_DIR}/Fig5_Testing_Dichotomy.png)\n",
        "after",
    ),
    (
        "### 8.1 Overview",
        f"\n![Figure 6: Falsification Procedure]({FIG_DIR}/Fig6_Falsification_Procedure.png)\n",
        "after",
    ),
    (
        "### 8.2 AS-F1 — Functional Duplication",
        f"\n![Figure 8: Overlap Matrix]({FIG_DIR}/Fig8_Overlap_Matrix.png)\n",
        "after",
    ),
    (
        "### 10.1 The decision",
        f"\n![Figure 7: Phase Status and Decision Outcomes]({FIG_DIR}/Fig7_Phase_Status.png)\n",
        "after",
    ),
    (
        "### 11.2 Scenarios S1–S6",
        f"\n![Figure 9: Evaluation Design]({FIG_DIR}/Fig9_Evaluation_Design.png)\n",
        "after",
    ),
]

for anchor, figure_md, position in insertions:
    idx = text.find(anchor)
    if idx == -1:
        print(f"WARN: anchor not found: {anchor!r}")
        continue
    end = text.find("\n", idx) + 1
    if end == 0:
        print(f"WARN: no newline after anchor: {anchor!r}")
        continue
    new_text = text[:end] + figure_md + text[end:]
    if new_text == text:
        print(f"WARN: no change at {anchor!r}")
        continue
    text = new_text
    print(f"OK: inserted figure after {anchor!r}")

MD.write_text(text, encoding="utf-8")
print("Done.")
