# Validation record

## Completed CAD checks

The final native KiCad 7.0.11 report records zero DRC violations, zero unconnected
pads and zero footprint errors. The board has 192 component pads, 56 nets and
77 vias. Schematic and PCB pad membership were compared with the pin map.
Connector orientation and the 9.144 mm motherboard socket spacing were checked.

The final silkscreen changes preserved all copper exports, solder-mask openings,
drills and outline data. Export timestamps were excluded from that comparison.
The submitted PCB and manufacturing ZIP are retained with frozen SHA-256 hashes.

## Portable audit

Run python3 source/verify_design.py from the repository root. This checks the
saved electrical geometry against design-baseline.json, actual PCB pad nets
against connection_map.json, recorded schematic netlist parity, connector pitch
and orientation, printed label height and the frozen manufacturing hashes.
It also checks local documentation links.

The default schematic comparison uses the recorded netlist. To review a changed
schematic, export a fresh KiCad netlist and pass --netlist PATH. The audit does
not run native DRC or prove that a stale recorded netlist represents new edits.

Run source/check_kicad.py using Python with pcbnew available for a new native DRC
report. Outputs go under build/ so recorded evidence is not silently replaced.

## Remaining hardware checks

The PCB has not been physically fitted, assembled or powered. No original-drive
timing, interrupt voltage margin, cable-length limit, boot behaviour or OS/driver
combination has been validated. Socket mating heights, actual connector body
dimensions, underside diode clearance and drive-cage clearance remain open.

Use HARDWARE-TEST-LOG.md to record evidence. Keep manufacturer fabrication tests,
assembled continuity checks and actual Amiga operation as separate results.
