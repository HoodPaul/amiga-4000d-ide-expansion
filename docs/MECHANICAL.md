# Mechanical dimensions

Positions below are top-view centres, relative to the board's upper-left corner.
Y increases towards the motherboard IDE socket edge.

| Reference | X centre (mm) | Y centre (mm) | Side |
|---|---:|---:|---|
| J3 | 29.210 | 6.096 | Top |
| J2 | 29.210 | 18.034 | Top |
| J5 | 29.210 | 29.972 | Top |
| J4 | 29.210 | 41.656 | Bottom |
| J1 | 29.210 | 50.800 | Bottom |

Outline: 58.42 × 55.88 mm. Nominal thickness: 1.6 mm. No mounting holes.
Connector pitch is 2.54 mm between adjacent columns and between rows.
The motherboard socket centres are 9.144 mm apart and aligned lengthwise.

The nominal standard 40-pin box-header body is 58.46 mm long, approximately
0.02 mm beyond each board edge. Actual header mouldings vary. Confirm the
chosen datasheets, including keying, tail dimensions and body overhang.
Regular routed-outline tolerance may make a finished edge slightly wider.

J1/J4 require matching mating heights. Both must seat fully without twisting
or bending the PCB or motherboard pins. The bottom diodes require clearance
above motherboard components. Check both drive-cage and cable-plug height.

Use [the 1:1 fit drawing](Fit_Check_1to1_A4.pdf) at 100% / Actual size. Measure
its 100 mm calibration bar. Disconnect the Amiga from power before checking.
The drawing checks the planned footprint positions; it does not confirm a
particular motherboard's fit or the finished assembly height.

This layout is intended for the A4000 Desktop. Other Amiga models and A4000T
connector arrangements have not been validated.
