# Electrical design

J1 is the motherboard IDE input. J2 is IDE A / Primary and J3 is IDE B / Secondary.
Most same-numbered IDE positions share the host bus. Host select signals choose
the device pair; each output is intended to carry a master and slave device.
The channels share data wiring and are not independent simultaneous transfer buses.

## Intentional connections

| Connection | Purpose |
|---|---|
| J1.37 to J2.37 | Primary select |
| J1.38 to J3.37 | Secondary select |
| J1.1 to J2.1, J3.1, J2.38 and J3.38 | Reset and the intended output pin-38 mapping |
| J1.31 to D1.1 and D2.1 | Host interrupt, diode cathodes |
| J2.31 to D1.2 | Primary interrupt, diode anode |
| J3.31 to D2.2 | Secondary interrupt, diode anode |
| J3.28 | Isolated secondary cable-select position |
| J3.34 | Isolated secondary diagnostic position |

Output pin 38 is not a conventional duplicated ATA control-register select.
The installed driver must support this type of four-device arrangement. Do not
change this connection merely to make it match a standard two-device cable.

D1/D2 combine the interrupt outputs at the host while isolating the outputs
from one another. Both parts are 1N4148. The banded end is cathode/pad 1/K.
Their operating voltage margins with the intended drives remain to be tested.

IDE grounds at positions 2, 19, 22, 24, 26, 30 and 40 share ground copper.
Other positions retain the connections listed in the machine-readable pin map.
There is a physical pad at position 20, but no drive-power supply is provided.
Do not power an adapter through pin 20. No DMA or active buffering is implemented.

## Floppy pass-through

J4 is the underside motherboard floppy socket. J5 is the top output. All 34
positions pass through. Pin 1 and odd positions 5 through 33 join ground.
Pin 3 is separate, as are the other signal positions. The floppy interface does
not participate in IDE selection or supply drive power.

Complete net data: [connection_map.json](../verification/connection_map.json)
and [pin_connections.csv](../verification/pin_connections.csv).
