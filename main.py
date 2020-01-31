import pyfirmata
import test


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
    test.testing_servos_on_arduino()

if __name__ == "__main__":
    main()
    
    