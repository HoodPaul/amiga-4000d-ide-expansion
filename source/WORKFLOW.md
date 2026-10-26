# Development and verification workflow

The saved root KiCad files are authoritative. The tools here inspect those files
or export a new manufacturing candidate; they do not generate or reroute the PCB.

1. Read AGENTS.md and the current handover. Check branch, HEAD and working tree.
2. Edit the saved CAD directly in KiCad. Preserve the submitted revision's electrical geometry unless the task specifically changes it.
3. Run the portable audit with Python 3.10 or newer and the pinned sexpdata dependency.
4. For native checking use KiCad's Python environment and run python3 source/check_kicad.py. Inspect build/drc_report.txt.
5. For schematic edits use kicad-cli sch export netlist --format kicadsexpr -o build/schematic.net Amiga4000_IDE_Expansion.kicad_sch, then python3 source/verify_design.py --netlist build/schematic.net.
6. Export a candidate with python3 source/export_fabrication.py. The output is build/fabrication, not the submitted REV0.1 folder.
7. Review the candidate in a Gerber viewer and compare all affected electrical and mechanical data. Update documentation and the revision record under explicit task scope.

The baseline fingerprints protect revision 0.1. An intentional electrical change
will fail that comparison until a new revision is deliberately reviewed and its
own baseline established. Do not update frozen hashes merely to silence a failure.

Opening or saving in a newer KiCad version may change file formatting. Compare
the electrical fingerprints and actual exports before accepting the change.
The public schematic's descriptive notes were updated for the initial GitHub
publication; its connectivity is unchanged.
