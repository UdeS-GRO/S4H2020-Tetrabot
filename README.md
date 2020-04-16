# Tetrabot

Tetrabot is a four-legged robot made out of wooden parts with 8 DOF (2 per leg) that draws inspiration from Boston Dynamics' Spot. The motors are controlled with an Adafruit servo driver and both the walking cycle and the UI are coded in Python on a Raspberry PI 3.

![ezgif com-optimize (1)](https://user-images.githubusercontent.com/43070865/75289747-f9056480-57ec-11ea-9d0a-09c0e0a104ec.gif)

## Getting Started

Here, you'll find documentation on the CAD and the code used to create this robot as well as instructions to assemble it and to set up the coding environment.
The Tetrabot Mechanical Team (TMT) designed two prototypes. The first prototype has been fully tested and is made primarily of wood. The second prototype is made primarily of 3D printed PLA. Each part can be printed but it was not fully assembled and tested with the electronics and the software.


### FIRST Prototype Prerequisites (hardware)

Before setting up the coding environment, you should make sure you have the following to build the robot:

```
Machines and tools:
  - A laser cutter
  - A 3D printer
  - Pliers
  - Cutters
Materials:
  - 1/8" thick wood planks
  - Wood glue
  - C7: Sandpaper
Electronics:
  - C1: 1 Raspberry PI 3
  - C2: 8 Hitec HS-422 Servo Motor
  - C3: 1 Adafruit PCA9685 16-Channel Servo Driver
  - C4: 5 V - 3.2 A power supply
  - C5: 4 Long female to female electrical wires
  - C6: 2 Crocodile clips with wires
Others:
  - Nuts and bolts of various sizes
```

The laser cutter should be used to cut the following parts out of the wood plank:

```
  - A1 : 1 top (optionnal) (CAD->Top)
  - A2 : 1 bottom (CAD->Body)
  - A3 : 2 sides (left/right) (CAD->Mur)
  - A4 : 2 other sides (front/back) (CAD->face)
  - A5 : 4 thighs (CAD->thight)
  - A6 : 4 tibias (CAD->tibia)
```

And the 3D printer should be used to print the following parts with PLA plastic.

```
  - B1 : 8 custom servo horns (CAD->Adapteur_servo_metal)
  - B2 : 4 feet (CAD->New Tetrabot->foot)
```

### FIRST Prototype Assembling

A step by step guide to building the robot. Make sure you have all of the parts mentioned above before beginning the assembly.

1. Glue the body

```
  1.1. Apply some glue to the indents of the bottom (A2) and the sides (A3 and A4).
  1.2. Assemble the parts and use pliers to keep the parts together.
  1.3. Let the assembly dry.
```

2. Assemble the legs

```
  2.2. Screw the servo horns (B1) to the thighs (A5).
  2.3. Screw the motors (C2) to the thighs (A5).
  2.4. Screw the servo horns (B1) to the tibias (A6).
  2.5. Cut squares of sandpaper (C7) and glue them under the feet (B2).
  2.6. Screw the feet (B2) to the tibias (A6).
  2.7. Fix the tibias' servo horns to the thighs' motors.
```

3. Assemble the robot

```
  3.1. Once the base is dry, screw the remaining servos (C2) to the sides from the inside of the base.
  3.2. Fix the thighs' servo horns to the base's motors.
```

4. Setup the electronics

```
  4.1. Weld the pins to the Adafruit driver (C3).
  4.2. Connect every servo wire to the driver like shown.
  4.3. Connect the driver (C3) to the PI using wires (C4) like shown.
  4.4. Connect the PI (C1) to a power source
  4.5. Plug in a keyboard and a mouse in the USB ports and a monitor in the HDMI port.
  4.6. Use wires to connect the Adafruit servo driver to a 5 V power supply.
```

5. After the software setup

```
  5.1. Unplug the monitor, screen, and mouse.
  5.2. Install (Don't glue!) the top of the robot. (If you have one)
```
### SECOND Prototype Prerequisites (hardware)

Every CAD that you need to make the final prototype is in the New Tetrabot folder. You will need these:

```
Machines and tools:
  - A 3D printer
  - Pliers
  - Cutters
Materials:
  - A7: Sandpaper
Electronics:
  - A1: 1 Raspberry PI 3
  - A2: 8 Hitec HS-422 Servo Motor
  - A3: 1 Adafruit PCA9685 16-Channel Servo Driver
  - A4: 5 V - 3.2 A power supply
  - A5: 4 Long female to female electrical wires
  - A6: 2 Crocodile clips with wires
Others:
  - Nuts and bolts of various sizes
```

The 3D printer should be used to print the following parts with PLA plastic. We used a MakerBot replicator+.

```
  - B1 : 1 base (CAD->New Tetrabot->Base2.01)
  - B2 : 4 feet (CAD->New Tetrabot->foot)
  - B3 : 4 whole thight (CAD->New Tetrabot->New_thigh_2)
  - B4 : 4 pierced thight (CAD->New Tetrabot->New_thigh)
  - B5 : 4 tibia (CAD->New Tetrabot->New_tibia)
  - B6 : 4 adapter (CAD->New Tetrabot->New_adapter)
```
The tibia and adapter should be printed with support with the part going in the motors facing up. The base, thigh and feet can be printed without support.

### SECOND Prototype Assembling

A step by step guide to building the robot. Make sure you have all of the parts mentioned above before beginning the assembly.

1. Assemble the legs

```
  1.1. Assemble and screw the two thighs (B3-B4) together with the adapter (B6) in the middle.
  1.2. Cut squares of sandpaper (A7) and glue them under the feet (B2).
  1.3. Screw the feet (B2) to the tibias (B5).
  1.4. Insert the tibias (B5) between the thighs.
  1.5. Screw the motors (A2) to the thighs (B4) while making sure that the motors are inserted in the tibias (B5).
```

2. Assemble the robot (some parts might collide, it was not fully tested)

```
  2.1. Insert the legs in the base (B1).
  2.2. Screw the motors (A2) to the base (B1) while making sure that the motors are in the thighs.
```

3. Setup the electronics

```
  4.1. Weld the pins to the Adafruit driver (A3).
  4.2. Connect every servo wire to the driver like shown.
  4.3. Connect the driver (A3) to the PI using wires (A4) like shown.
  4.4. Screw the driver (A3) to the base (B1).
  4.5. Connect the PI (A1) to a power source.
  4.6. Plug in a keyboard and a mouse in the USB ports and a monitor in the HDMI port.
  4.7. Use wires to connect the Adafruit servo driver to a 5 V power supply.
```


### Prerequisites (software)

The tutorials that follow will state what you need to install their respective software.

### Installing

Follow this guide to install
[CircuitPython](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux) on your Pi.

Follow this guide to setup your RaspberryPi with the
[Adafruit 16 Channel Servo Driver](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux).

Connect the servos to the drive:

```
Follow step 4 of the assembling tutorial above.
```

Once everything is set up, run `python3 servo.py` to make Tetrabot stand up.

You will need to change the `offset` values in `servo.py` until its legs are straight and perpendicular to the ground.

```
off_haut_gauche = [?, ?]
off_bas_gauche = [?, ?]
off_haut_droite = [?, ?]
off_bas_droite = [?, ?]

offset = [off_haut_gauche, off_haut_droite, off_bas_gauche, off_haut_gauche]
```

_Once the legs are straight, the setup is finished._

Run `python3 main.py` to start **Tetrabot**.

## Authors

- **Mathis Gagnon** - _Initial work_ - [MathisGagnon](https://github.com/mathisgag)
- **Alexandre Lafleur** - _Initial work_ - [AlexandreLafleur](https://github.com/alexandrelafleur)
- **Tristan Roy** - _Initial work_ - [TristanRoy](https://github.com/Tristan-01)
- **Félix-Antoine Toussaint** - _Initial work_ - [FélixAntoineToussaint](https://github.com/FAT8888)
- **Alexis Tremblay-Lebel** - _Initial work_ - [AlexisTremblayLebel](https://github.com/AlexisTB)
- **Philippe Turcotte** - _Initial work_ - [PhilippeTurcotte](https://github.com/turcottep)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

- ZenHub Agile Project Management
- Authors of the CircuitPython and Adafruit tutorials
- Boston Dynamics' Spot
- PurpleBooth README.md template
