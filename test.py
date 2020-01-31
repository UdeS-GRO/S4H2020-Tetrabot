import time

def testing_servos_on_arduino():
    while True:
        servos[2].write(angle(110))
        servos[3].write(angle(160))
        time.sleep(2)
        servos[2].write(angle(160))
        servos[3].write(angle(220))
        time.sleep(2)
