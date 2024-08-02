# Watch Laser Trip Wire with Discord Bot 
This project utilized two Discord bots to watch a laser trip wire where a master bot,
named Wire_Bot, a.k.a Hal, who responded to certain commands in chat. The images bellow demonstrate what prompts Hal would respond to, and the last two pictures show a simple setup for the trip wire.

<p align="center">
  <img title='Bot Chat Ex. One' src=docs/images/image01.png width="650">
  <img title='Bot Chat Ex. Two' src=docs/images/image02.png width="650">
</p>

<p align="center">
  <img title='Trip Wire Pic One' src=docs/images/tripWirePic01.png width="300">
  <img title='Trip Wire Pic Two' src=docs/images/tripWirePic02.png width="300">
</p>

# Hardware & Circuits
Here's a list of components used in project:

| |Components |
|--| --|
|1| Raspberry Pi 3B+ |
|2| Light Dependent Resistor (LDR)|
|3| 1uF Capacitor|
|4| N-MOSFET|
|5| 470Ω Resistor| 
|6| 5V Laser Diode|

Next, lets take a look at the two circuits used in this project.
### Light Sensor Circuit 
<p align="center">
  <img title='Light Sensor Circuit' src=docs/circuits/light_sensor.png width="800">
</p>

### Laser Circuit 
<p align="center">
  <img title='Laser Circuit' src=docs/circuits/laser.png width="800">
</p>