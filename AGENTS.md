# AI instructions: Amiga 4000D IDE Expansion

## Read first

Read README.md, docs/AI-HANDOVER.md, docs/README.md and the task-specific guide before editing. Verify the current branch, HEAD and working tree. This is a KiCad hardware project. Do not introduce a web application, database or unrelated framework.

The root KiCad PCB, schematic, project and A4000_Local.pretty define the design. Use current repository evidence and Paul's latest instructions. Do not silently substitute old chat values for file contents.

## Preserve the submitted revision

Paul reports revision 0.1 was submitted for PCB fabrication on 26 October 2026. Do not mark boards received, assembled, mechanically verified or tested without new evidence. The reviewed quote is not proof of final order quantity, finish or copper weight.

Preserve fabrication/REV0.1 and verification/ordered-revision.json. Never overwrite an ordered revision's manufacturing package as incidental cleanup. Export any new manufacturing candidate into a separate build or revision folder. Record the actual revision and SHA-256 hashes.

Preserve routing, pads, component placement, outline, filled copper and electrical mapping unless the user requests a design change. A documentation or artwork task does not authorise electrical changes. Compare electrical fingerprints before and after artwork work. Native DRC and a matching netlist remain necessary for circuit changes.

## Fixed electrical and mechanical facts

- Revision 0.1: 58.42 × 55.88 mm, four copper layers, 1.6 mm nominal thickness.
- F.Cu/B.Cu carry signals. In1.Cu and In2.Cu are ground planes.
- Motherboard sockets J1 and J4 are underneath, lengthwise aligned, 9.144 mm apart between centres. Both need matching mating heights.
- J2 is IDE A / Primary. J3 is IDE B / Secondary. J5 is floppy pass-through.
- D1/D2 are underside 1N4148 DO-35 parts at 7.62 mm lead pitch. Both cathodes, pad 1 / band / K, connect to J1.31.
- Host J1.37 goes to J2.37. Host J1.38 goes to J3.37. J2.38 and J3.38 join host reset J1.1. This mapping is intentional.
- J3.28 and J3.34 are isolated. Do not join them to the host or primary channel.
- Floppy pin 3 stays a separate pass-through net. Documented floppy grounds are pin 1 and odd pins 5 through 33.
- IDE position 20 is not a power supply. There is no drive power circuit, DMA implementation or active bus buffer.

## Appearance and documentation

Maintain the black-PCB appearance, white printing and supplied underside logos. REV 0.1 reads at bottom left from the rear. Connector references remain below their pin-1 labels. Pin-1 arrows are within the nominal upper plastic rails. All printed labels are at least 1.0 mm high with 0.15 mm strokes.

Use the public project description and existing documentation style. Keep the artwork credits and KiCad library notices. No project-wide standard licence has been selected; do not assign one without Paul's instruction. Use British English and avoid em dashes.

## Validation and completion

Use source/verify_design.py for the portable saved-data audit. Read docs/VALIDATION.md for its exact scope. For native checks use source/check_kicad.py with KiCad's Python module. Export a fresh schematic netlist when checking schematic changes, rather than relying on the recorded netlist.

After a change, update the authoritative guide, current handover and changelog as appropriate. Describe the actual checks and outstanding hardware work. Do not suppress findings or describe a CAD check as a hardware test. Keep existing manufacturer review and hardware results separate.

For repository changes use a focused branch/PR unless the current request explicitly authorises publication. Do not purchase PCBs, replace submitted manufacturing data, or send messages to others without task-specific authorisation. Do not publish private order links, addresses, credentials or customer information.
