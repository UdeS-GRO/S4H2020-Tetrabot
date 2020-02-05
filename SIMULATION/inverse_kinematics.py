def inverse_kinematic(x, y, a1, a2):
    num = x ** 2 + y ** 2 - a1 ** 2 - a2 ** 2
    denum = 2 * a1 * a2
    q2 = math.acos(num / denum)

    num = a2 * math.sin(q2)
    denum = a1 + a2 * math.cos(q2)
    q1 = math.atan(y / (x + 0.000001)) - math.atan(num / (denum + 0.000001))
    print("q1 =", 180*q1/math.pi)
    print("q2=", 180*q2/math.pi)
    return q1, q2
