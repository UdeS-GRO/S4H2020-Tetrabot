from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
import time


offset_th_0 = [107,97,124,74]
offset_th_1 = [157,141,20,2]

def move(thigh, knee):
    kit.servo[0].angle = offset_th_0[0] + thigh[0]
    kit.servo[1].angle = offset_th_1[0] - knee[0]

    kit.servo[2].angle = offset_th_0[1] + thigh[1]
    kit.servo[3].angle = offset_th_1[1] - knee[1]

    kit.servo[4].angle = offset_th_0[2] - thigh[2]
    kit.servo[5].angle = offset_th_1[2] + knee[2]

    kit.servo[6].angle = offset_th_0[3] - thigh[3]
    kit.servo[7].angle = offset_th_1[3] + knee[3]

if __name__ == "__main__":
    angles_0 = [-40, -40, -40, -40]
    angles_1 = [80, 80, 80, 80]
    move([0,0,0,0], [0,0,0,0])
    time.sleep(2)
    move(angles_0, angles_1)
    