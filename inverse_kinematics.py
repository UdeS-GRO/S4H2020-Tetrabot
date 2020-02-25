import math


# Function to find the 2 angles q1,q2 for each joints of the robot
def inverse_kinematic(x, y, a1, a2):
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
