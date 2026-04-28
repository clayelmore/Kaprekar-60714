#!/bin/bash
#
# reproduce.sh — runs the complete d=7 audit package end-to-end.
#
# Usage: ./reproduce.sh
#
# Stages (in order):
#   1. verify_setup.py          — 30-second sanity check
#   2. audit_60714_d7.py        — Run A, ~3 seconds
#   3. classify_d7_full.py      — Run B, ~5-30 minutes (with Numba parallel)
#   4. d7_outcome_verifier.py   — Run C, ~1-3 hours
#
# Each stage's outputs are written to the current directory. If any stage
# fails, the script aborts.
#
# To run only a subset, comment out the unwanted stages or invoke the
# individual scripts directly.

set -e

echo "=========================================="
echo "  d=7 audit package — full reproduction"
echo "=========================================="
echo

# --- Stage 1: setup verification ---
echo "Stage 1/5: verify_setup.py"
echo "---"
python3 verify_setup.py
echo

# --- Stage 2: 60714 d=7 audit ---
echo "Stage 2/5: audit_60714_d7.py"
echo "---"
python3 audit_60714_d7.py
echo

# --- Stage 3: 60714 d=8 audit (even ladder) ---
echo "Stage 3/5: audit_60714_d8.py"
echo "---"
python3 audit_60714_d8.py
echo

# --- Stage 4: full d=7 sound enumeration ---
echo "Stage 4/5: classify_d7_full.py"
echo "---"
echo "Note: this is the long stage. Estimated 5-30 minutes with Numba parallel,"
echo "      or several hours single-threaded. The script supports crash-resume."
echo
python3 classify_d7_full.py
echo

# --- Stage 5: 52-fp outcome verifier ---
echo "Stage 5/5: d7_outcome_verifier.py"
echo "---"
echo "Note: this is the longest stage. Estimated 1-3 hours."
echo "      Progress is checkpointed after every fp."
echo
python3 d7_outcome_verifier.py
echo

echo "=========================================="
echo "  All stages complete."
echo "=========================================="
echo
echo "Output files:"
echo "  audit_60714_d7.json          — Run A  results (d=7 odd ladder)"
echo "  audit_60714_d8.json          — Run A2 results (d=8 even ladder)"
echo "  d7_classification.json       — Run B: full universal-fp catalog"
echo "  d7_fps.txt                   — Run B: fp list (text)"
echo "  d7_progress.log              — Run B: progress trace"
echo "  d7_verified_outcomes.json    — Run C: full per-fp data"
echo "  d7_summary.txt               — Run C: one-line-per-fp summary"
echo "  d7_classifier_analysis.txt   — Run C: cycle-signature cross-tab"
echo
echo "Send these back for analysis."
