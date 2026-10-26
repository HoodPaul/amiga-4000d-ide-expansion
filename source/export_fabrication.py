#!/usr/bin/env python3
"""Export a new candidate under build/, preserving the submitted revision."""
from pathlib import Path
import subprocess,shutil,zipfile
root=Path(__file__).resolve().parents[1]
cli=shutil.which('kicad-cli')
if not cli:raise SystemExit('kicad-cli must be available on PATH.')
output=root/'build/fabrication';output.mkdir(parents=True,exist_ok=True)
board=root/'Amiga4000_IDE_Expansion.kicad_pcb'
subprocess.run([cli,'pcb','export','gerbers','--output',str(output)+'/',
    '--layers','F.Cu,In1.Cu,In2.Cu,B.Cu,F.Silkscreen,B.Silkscreen,F.Mask,B.Mask,Edge.Cuts',str(board)],check=True)
subprocess.run([cli,'pcb','export','drill','--output',str(output)+'/',
    '--excellon-separate-th',str(board)],check=True)
with zipfile.ZipFile(root/'build/A4000D_IDE_Expansion_candidate.zip','w',zipfile.ZIP_DEFLATED) as z:
    for f in sorted(output.iterdir()):
        if f.is_file():z.write(f,f.name)
print('Candidate exported under build/. Review before manufacturing.')
