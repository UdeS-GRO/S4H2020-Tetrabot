import pyfirmata
import time

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
        

    i = 1
    print("Starting ...")

    while True:
        led.write(1)
        servos[2].write(30)
        servos[3].write(30)
        time.sleep(2)
        led.write(0)
        servos[2].write(90)
        servos[3].write(90)
        time.sleep(2)

def walk():
    pass


if __name__ == "__main__":
    main()
    