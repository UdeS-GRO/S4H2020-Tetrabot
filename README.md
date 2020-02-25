# Tetrabot

Tetrabot is a four-legged robot made out of wooden parts with 8 DOF (2 per leg) that draws inspiration from Boston Dynamics' Spot. The motors are controled with an Adafruit servo driver and both the walking cycle and the UI are coded in Python on a Raspberry PI 3.

![ezgif com-optimize (1)](https://user-images.githubusercontent.com/43070865/75289747-f9056480-57ec-11ea-9d0a-09c0e0a104ec.gif)

## Getting Started

Here, you'll find documentation on the CAD and the code used to create this robot as well as instructions to assemble it and to setup the coding environment.

### Prerequisites (hardware)

Before setting up the coding environment, you should make sure you have the following in order to build the robot:

```
Machines and tools:
  - A laser cutter
  - A 3D printer
  - Pliers
  - Cutters
Materials:
  - 1/8" thick wood planks
  - Wood glue
  - Sand paper
Electronics:
  - 1 Raspberry PI 3
  - 8 Hitec HS-422 Servo Motor
  - 1 Adafruit PCA9685 16-Channel Servo Driver
  - 5 V - 3.2 A power supply
  - 4 Long female to female electrical wires
  - 2 Crocodile clips with wires
Others:
  - Nuts and bolts of various sizes
```

The laser cutter should be used to cut the following parts out of the wood plank:

```
  - 1 top (optionnal)
  - 1 bottom
  - 2 sides (left/right)
  - 2 other sides (front/back)
  - 4 thighs
  - 4 tibias
```

And the 3D printer should be used to print the following parts with PLA plastic.

```
  - 8 custom servo horns
  - 4 feet
```

### Assembling

A step by step guide to build the robot. Make sure you have all of the parts mentionned above before beginning the assembly.

1. Glue the body

```
  1.1. Apply some glue to the indents of the bottom and the sides.
  1.2. Assemble the parts and use pliers to keep the parts together.
  1.3. Let the assembly dry.
```

2. Assemble the legs

```
  2.2. Screw the servo horns to the thighs.
  2.3. Screw the motors to the thighs.
  2.4. Screw the servo horns to the tibias.
  2.5. Cut squares of sand paper and glue them under the feet.
  2.6. Screw the feet to the tibias.
  2.7. Fix the tibias' servo horns to the thighs' motors.
```

3. Assemble the robot

```
  3.1. Once the base is dry, screw the remaining servos to the sides from the inside of the base.
  3.2. Fix the thighs' servo horns to the base's motors.
```

4. Setup the electronics

```
  4.1. Weld the pins to the Adafruit driver.
  4.2. Connect every servo wire to the driver like shown.
  4.3. Connect the driver to the PI like shown.
  4.4. Connect the PI to a power source. and
  4.5. Plug in a keyboard and a mouse in the USB ports and a monitor in the HDMI port.
  4.6. Use wires to connect the Adafruit servo driver to a 5 V power supply.
```

5. After the software setup

```
  5.1. Unplug the monitor, screen and mouse.
  5.2. Install (Don't glue!) the top of the robot. (If you have one)
```

### Prerequisites (software)

The tutorials that follow will state what you need to install their respective softwares.

### Installing

Follow this guide to install
[CircuitPython](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux) on your Pi.

Follow this guide to setup your RaspberryPi with the
[Adafruit 16 Channel Servo Driver](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux).

Connect the servos to the drive:

```
Follow step 4 of the assembling tutorial above.
```

Once everything is setup, run `python3 servo.py` to make Tetrabot stand up.

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
