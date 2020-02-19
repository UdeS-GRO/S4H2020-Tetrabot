from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)

offset_th_0 = [90,70,115,93]
offset_th_1 = [140,127,40,15]

def init_servos():
    for x in range(len(offset_th_0)):
        offset=13
        if x<2:
            offset_th_0[x] -= offset
        else:
            offset_th_0[x] += offset

    for i in range(0,7):
        kit.servo[i].actuation_range = 180
        kit.servo[i].set_pulse_width_range(450, 2550)


def move(thigh, knee):
    kit.servo[0].angle = offset_th_0[0] + .9*thigh[0]
    kit.servo[1].angle = offset_th_1[0] - .9*knee[0]

    kit.servo[2].angle = offset_th_0[1] + .9*thigh[1]
    kit.servo[3].angle = offset_th_1[1] - .9*knee[1]

    kit.servo[4].angle = offset_th_0[2] - .9*thigh[2]
    kit.servo[5].angle = offset_th_1[2] + .9*knee[2]

    kit.servo[6].angle = offset_th_0[3] - .9*thigh[3]
    kit.servo[7].angle = offset_th_1[3] + 1.25*knee[3]

if __name__ == "__main__":
    init_servos()
    th1 = 0
    th2 = 0
    angles_0 = [th1, th1, th1, th1]
    angles_1 = [th2, th2, th2, th2]
    move([0,0,0,0], [0,0,0,0])
    time.sleep(2)
    move(angles_0, angles_1)
    