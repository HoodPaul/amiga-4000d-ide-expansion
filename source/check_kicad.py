#!/usr/bin/env python3
"""Run native KiCad DRC without overwriting recorded revision evidence."""
from pathlib import Path
import sys
try:
    import pcbnew
except ImportError:
    raise SystemExit('Run with the Python environment that provides KiCad pcbnew.')

root=Path(__file__).resolve().parents[1]
output=root/'build';output.mkdir(exist_ok=True)
board=pcbnew.LoadBoard(str(root/'Amiga4000_IDE_Expansion.kicad_pcb'))
report=output/'drc_report.txt'
pcbnew.WriteDRCReport(board,str(report),pcbnew.EDA_UNITS_MILLIMETRES,True)
text=report.read_text();print(text)
if 'Found 0 DRC violations' not in text or 'Found 0 unconnected pads' not in text:sys.exit(1)
