import math


def inverse_kinematic(x, y, a1, a2):
    """
    :param x: x position of end effector
    :param y: y position of end effector
    :param a1: length of member 1
    :param a2: length of member 2

    :return: angles of a 2 joint same plane robot arm
    """
    # find q2 angle of the second joint
    num = x ** 2 + y ** 2 - a1 ** 2 - a2 ** 2
    denum = 2 * a1 * a2
    q2 = math.acos(num / denum)

    # find q1 angle of the first joint
    num = a2 * math.sin(q2)
    denum = a1 + a2 * math.cos(q2)
    epsilon = 0.000001
    q1 = math.atan(y / (x + epsilon)) - math.atan(num / (denum + epsilon))
    return q1, q2
