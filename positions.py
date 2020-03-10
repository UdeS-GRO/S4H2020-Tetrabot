from inverse_kinematics import inverse_kinematic


def get_positions_from_walk_sequence():
    """
     @return: array of delta positions of 2 joints for each of the 4 feet from walk sequence
     """

    delta_steps = []
    yinit_back = 140
    yinit_front = 140
    xstep = 60

    #penche avant
    delta_steps.append([[0, yinit_front], [0, yinit_front], [0, yinit_back], [0, yinit_back]])
  
    # Walk it like i talk it #  Front wheelie -| pattes arrieres -| pattes avant
    #  Front wheelie
    delta_steps.append([[0, 20], [0, 20], [0, 20], [0, 20]])
    #  Avance la patte arriere gauche 
    delta_steps.append([[0, 0], [0, 0], [0, -35], [0, 0]])
    delta_steps.append([[0, 0], [0, 0], [40, 0], [0, 0]])
    delta_steps.append([[0, 0], [0, 0], [0, 35], [0, 0]])
    #  Avance la patte arriere droite 
    delta_steps.append([[0, 0], [0, 0], [0, 0], [0, -35]])
    delta_steps.append([[0, 0], [0, 0], [0, 0], [40, 0]])
    delta_steps.append([[0, 0], [0, 0], [0, 0], [0, 35]])
    #  cancel Front wheelie
    delta_steps.append([[0, -20], [0, -20], [0, -20], [0, -20]])
    #  Avance la patte avant gauche 
    delta_steps.append([[0, -35], [0, 0], [0, 0], [0, 0]])
    delta_steps.append([[40, 0], [0, 0], [0, 0], [0, 0]])
    delta_steps.append([[0, 35], [0, 0], [0, 0], [0, 0]])
    #  Avance la patte avant droite 
    delta_steps.append([[0, 0], [0, -35], [0, 0], [0, 0]])
    delta_steps.append([[0, 0], [40, 0], [0, 0], [0, 0]])
    delta_steps.append([[0, 0], [0, 35], [0, 0], [0, 0]])
    #  Pull-in Marois
    delta_steps.append([[-40, 0], [-40, 0], [-40, 0], [-40, 0]])

    return get_positions_from_delta_positions(delta_steps)


# get the delta-positions (mouvement for each joint to perform)
def get_positions_from_delta_positions(delta_steps):
    """
     @param delta_steps: array of delta positions of 2 joints for each of the 4 feet
     @return: array of positions of 2 joints for each of the 4 feet
     """

    steps = []
    for i, step in enumerate(delta_steps):
        if i == 0:
            steps.append(delta_steps[i])
        else:
            for j, delta in enumerate(step):
                delta_steps[i][j][0] = delta_steps[i][j][0] + delta_steps[i - 1][j][0]
                delta_steps[i][j][1] = delta_steps[i][j][1] + delta_steps[i - 1][j][1]
            steps.append(step)
    return steps


# Augments resolution of the steps to have a smoother walking sequence for each joint
def steps_smoother(steps, resolution):
    """
     @param delta_steps: array of delta positions of 2 joints for each of the 4 feet
     @return: array of positions of 2 joints for each of the 4 feet
     """
    smoothed_steps = []
    for i in range(len(steps)):
        step = steps[i]
        next_step = steps[(i + 1) % len(steps)]
        for j in range(resolution):
            smoothed_step = []

            for k in range(4):
                positions = step[k]
                next_positions = next_step[k]
                pos0 = positions[0] + j * ((next_positions[0] - positions[0]) / resolution)
                pos1 = positions[1] + j * ((next_positions[1] - positions[1]) / resolution)
                smoothed_step.append([pos0, pos1])
            smoothed_steps.append(smoothed_step)

    return smoothed_steps


def get_angles_from_positions(steps):
    """
     @param steps: array of positions of 2 joints for each of the 4 feet
     @return: array of angles for 2 joints for each of the 4 feet
     """

    angle_steps = []
    for step in steps:
        angle_step = []
        for leg in step:
            angle0, angle1 = inverse_kinematic(leg[1], leg[0], 70, 100)
            angle_step.append([angle0, angle1])
        angle_steps.append(angle_step)

    return angle_steps
