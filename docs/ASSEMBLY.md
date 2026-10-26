# Assembly and first use

Use BOM.csv. No ICs, resistors or capacitors are fitted to this board.

## Parts selection

- J1: female 2×20 PCB solder-tail socket. J4: female 2×17 PCB solder-tail socket. Both use 2.54 mm row/column pitch and need equal mating heights.
- J2/J3: vertical male 2×20 shrouded IDC box headers. J5: vertical male 2×17 shrouded IDC box header. All use 2.54 mm pitch.
- D1/D2: 1N4148 axial DO-35/SOD27, bent to 7.62 mm lead spacing.

Check the actual body dimensions, mating depth, solder-tail length and pin-20
keying. IDC ribbon-cable plugs are not substitutes for J1/J4 PCB sockets.
No specific connector manufacturer part number is approved yet.

## Fitting

1. Inspect the bare PCB for damaged plating, blocked holes or bridges.
2. Fit D1/D2 underneath. Both cathode bands go to pad 1, marked K. Keep the bodies low without stressing the glass packages.
3. Fit J1/J4 underneath and J2/J3/J5 above. Confirm pin 1 before soldering and ensure the two sockets sit square at equal heights.
4. Inspect every joint. Ground-plane pads can require more heat during hand soldering.
5. With all power disconnected, check continuity against the pin map. Check the diode paths in diode mode and check for unintended shorts.
6. Check motherboard alignment and clearance, including the underside diodes. Never force both sockets into place.

## First functional tests

Begin with a spare, known-working drive on IDE A and its normal separate power
connection. Verify a stable boot and repeated read/write operations. Test the
floppy pass-through, then the secondary IDE output with compatible software.
Add slave devices only after single-device tests pass. Keep cables short and
set master/slave jumpers explicitly.

Use backed-up test media and record results in HARDWARE-TEST-LOG.md. Submission
for fabrication and a successful manufacturer continuity test do not establish
Amiga compatibility or successful assembly.
