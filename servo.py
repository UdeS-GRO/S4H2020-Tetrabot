from adafruit_servokit import ServoKit
from math import pi

def rad_to_deg(rad):
    return rad*180/pi

kit = ServoKit(channels=16)

off_haut_gauche = [88, 155]
off_haut_droite = [94, 35]
off_bas_gauche = [89, 148]
off_bas_droite = [97, 8]

offset = [off_haut_gauche, off_haut_droite, off_bas_gauche, off_bas_droite]


def format_step_for_servo(step):
    formatted_step = []
    for leg_angles in step:
        angle0 = rad_to_deg(leg_angles[0]) + 90
        angle1 = rad_to_deg(leg_angles[1])
        formatted_step.append([angle0, angle1])

    return formatted_step


def init_servos():
    """
    Init the range of servos for the corrected pulse (in ms)
     """
    for i in range(0, 7):
        kit.servo[i].actuation_range = 180
        kit.servo[i].set_pulse_width_range(450, 2550)


def move(step):
    position = format_step_for_servo(step)
    """
     @param position: position array for each joint
     """
    # haut gauche
    kit.servo[0].angle = offset[0][0] + .9 * position[0][0]
    kit.servo[1].angle = offset[0][1] - .9 * position[0][1]
    # haut droite
    kit.servo[2].angle = offset[1][0] - .9 * position[1][0]
    kit.servo[3].angle = offset[1][1] + .9 * position[1][1]
    # bas gauche
    kit.servo[4].angle = offset[2][0] + .9 * position[2][0]
    kit.servo[5].angle = offset[2][1] - .9 * position[2][1]
    # bas droite
    kit.servo[6].angle = offset[3][0] - .9 * position[3][0]
    kit.servo[7].angle = offset[3][1] + 1.25 * position[3][1]


if __name__ == "__main__":
    init_servos()
    thet = -3*pi/4
    thet2 = pi/2
    move([[thet, thet2], [thet, thet2], [thet, thet2], [thet, thet2]])

    # offset_th_0 = [90,70,115,93]
    # offset_th_1 = [140,127,40,15]

    # kit.servo[0].angle = offset_th_0[0] + .9*thigh[0]
    # kit.servo[1].angle = offset_th_1[0] - .9*knee[0]

    # kit.servo[2].angle = offset_th_0[1] + .9*thigh[1]
    # kit.servo[3].angle = offset_th_1[1] - .9*knee[1]

    # kit.servo[4].angle = offset_th_0[2] - .9*thigh[2]
    # kit.servo[5].angle = offset_th_1[2] + .9*knee[2]

    # kit.servo[6].angle = offset_th_0[3] - .9*thigh[3]
    # kit.servo[7].angle = offset_th_1[3] + 1.25*knee[3]
