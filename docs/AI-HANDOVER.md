# Current AI handover

Updated: **26 October 2026**. Current PCB revision: **0.1**.

## Purpose and current state

Amiga 4000 Desktop IDE expansion with a matching black-PCB appearance. Two IDE
outputs support an intended master/slave pair each, with compatible software.
A 34-pin floppy pass-through also provides a second motherboard support point.

Paul reports that the final PCB files have been submitted for fabrication.
No received board, approved connector part number, assembled fit or functional
test has yet been recorded. Do not turn the submission into an operating claim.

## Authoritative files

- Root Amiga4000_IDE_Expansion.kicad_pcb, .kicad_sch and .kicad_pro.
- A4000_Local.pretty and fp-lib-table. Symbols are embedded in the schematic.
- BOM.csv and verification/connection_map.json.
- fabrication/REV0.1/A4000D_IDE_Expansion_Rev0_1_Gerbers.zip is the exact submitted ZIP. Preserve its bytes and the raw files.
- verification/ordered-revision.json contains the frozen PCB and manufacturing hashes. The public schematic has updated descriptive notes, with unchanged pin connectivity.

The delivered PCB is byte-identical to the PCB used for the final submission.
Keep that distinction from schematic documentation updates and future exports.

## Design facts to retain

Four layers, 58.42 × 55.88 mm, 1.6 mm nominal. Both internal layers are ground.
J1/J4 are underside motherboard sockets, aligned lengthwise and 9.144 mm apart.
J2/J3/J5 are top-side headers. D1/D2 and the supplied logos are underneath.
All connector row/column pitches are 2.54 mm. Diode lead spacing is 7.62 mm.

The intentional pin exceptions are detailed in ELECTRICAL.md. In particular,
output pin 38 is reset, J3.37 uses host J1.38, and J3.28/J3.34 are isolated.
Do not replace that mapping with a fully parallel IDE splitter. Floppy pin 3
remains a separate signal. No drive power is supplied.

The final printing uses 1 mm minimum labels and 0.15 mm strokes. The top IDE B
outline is complete; its top line is lowered slightly to clear the title. All
three pin-1 triangles sit in the nominal upper plastic rails. Preserve the
underside logo positions and rear bottom-left REV 0.1 printing.

## Checks completed

KiCad 7.0.11: zero DRC violations, zero unconnected pads and zero footprint
errors. 192 component pads, 56 nets and 77 vias. Schematic/PCB pin maps match.
Final printing updates preserved the copper, solder-mask openings, drills and
outline exports. The repository's portable audit checks the frozen electrical
fingerprints and manufacturing hashes; it is not a hardware simulation.

## Next actions

1. Record receipt and inspection of the manufactured boards.
2. Select socket/header part numbers from actual datasheets. Match J1/J4 mating heights and check pin-20 keying.
3. Verify board alignment, diode underside clearance, drive cage and cable plug clearance.
4. Assemble one board, inspect soldering and check all connections and diode directions while unpowered.
5. Test a spare drive on IDE A, then the floppy pass-through, IDE B and two-device master/slave cables.
6. Record exact motherboard revision, OS/driver, drive models, jumper settings and cable lengths in HARDWARE-TEST-LOG.md.

No confirmed OS unit numbering, boot behaviour, maximum cable length or operating
speed is available. Keep those open until measured. Use source/WORKFLOW.md before
changing CAD or generating new manufacturing candidates.
