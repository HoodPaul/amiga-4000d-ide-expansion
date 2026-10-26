# Fabrication settings and submission record

## Submission record

On 26 October 2026 Paul reported that the final revision 0.1 package had been
submitted for PCB fabrication. The final paid order options, quantity and
manufacturer order reference are not recorded. No board receipt, assembly or
functional test is confirmed.

The submitted ZIP is retained at
[A4000D_IDE_Expansion_Rev0_1_Gerbers.zip](../fabrication/REV0.1/A4000D_IDE_Expansion_Rev0_1_Gerbers.zip).
Its bytes are unchanged from the supplied final ZIP. SHA-256 hashes are recorded
in [ordered-revision.json](../verification/ordered-revision.json).

## Design requirements and suggested options

| Setting | Selection |
|---|---|
| Material | FR-4 |
| Dimensions | 58.42 × 55.88 mm |
| Layers | Four |
| Sequence | F.Cu / In1.Cu / In2.Cu / B.Cu |
| Thickness | 1.6 mm nominal |
| Mask / silkscreen | Black on both faces / white |
| Outer copper | 1 oz |
| Inner copper | Standard 0.5 oz is sufficient for the ground planes |
| Finish | ENIG 1 microinch for the gold-pad appearance; lead-free HASL is an alternative |
| Minimum via drill | 0.30 mm; actual via copper diameter is 0.60 mm |
| Via covering | Ink-plugged was selected in the reviewed quote |
| Outline tolerance | Regular ±0.2 mm was selected in the reviewed quote |
| Manufacturer mark | Remove mark |
| Electrical test | Full flying-probe test |
| Production file confirmation | Yes |
| Custom stackup / impedance control | Not required by this design |
| Assembly | Bare PCB order; components fitted separately |

The reviewed quote showed 10 boards, 1 oz inner copper and ENIG. The subsequent
recommendation was 0.5 oz inner copper to avoid an unnecessary surcharge.
Do not treat the quote as confirmation of the final order selections.

For ink-plugged vias, use this remark:

> Plug only the 0.30 mm vias. Leave all 0.80 mm diode holes and 1.00 mm connector holes open.

The Gerbers define copper and printing shapes. Mask colour, laminate thickness,
copper weight and finish are order-form selections. Neither successful upload
nor manufacturer continuity testing validates the circuit's operation.

Keep this revision's submitted files unchanged. Any future candidate needs a
new export folder, current native checks and a documented comparison.
