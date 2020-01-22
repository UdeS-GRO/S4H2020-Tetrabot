import pyfirmata
import time
import math

def main():
    board = pyfirmata.Arduino('/dev/cu.usbmodem14401')

    it = pyfirmata.util.Iterator(board)
    it.start()

    digital_input = board.get_pin('d:10:i')
    led = board.get_pin('d:13:o')
    
    servos = []
    for i in range(4):
        pin = board.get_pin('d:' + str(i + 2) + ':s')
        servos.append(pin) 
        

    print("Starting ...")

    while True:
        servos[2].write(angle(110))
        servos[3].write(angle(160))
        time.sleep(2)
        servos[2].write(angle(160))
        servos[3].write(angle(220))
        time.sleep(2)


def angle(angle):
    return angle * 255 / 360


def get_position_from_angles(a1, a2):
    l1 = 10
    l2 = 10

    angle_1 = a1
    x_cuisse = l1 * math.cos(angle_1)
    y_cuisse = l1 * math.sin(angle_1)

    angle_2 = math.pi - a1 - a2
    x_mollet = l2 * math.cos(angle_2)
    y_mollet = l2 * math.sin(angle_2)

    x_tot = x_cuisse + x_mollet
    y_tot = y_cuisse + y_mollet
    print(x_tot)
    print(y_tot)


if __name__ == "__main__":
    main()
    # get_position_from_angles(math.pi / 2, 0)
    # get_angles_from_position(0, 20)
    