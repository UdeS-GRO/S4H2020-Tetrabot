from src.inverse_kinematics import inverse_kinematic


def get_positions_from_walk_sequence():
    """
    @return: array of delta positions ofxstep 2 joints for each of the 4 feet from walk sequence
    """

    delta_steps = []
    yinit = 150
    xstep = 60
    y_up = -12.5
    delta_wheelie = -20
    x_init = -xstep
    x_offset = 25

    # initial positions
    delta_steps.append([[x_init + 20, yinit], [x_init + 20, yinit], [x_init, yinit], [x_init, yinit]])

    for _ in range(10):
        #  Puts the back-left leg forward
        delta_steps.append([[0, 0], [0, 0], [0, y_up], [0, 0]])
        delta_steps.append([[0, 0], [0, 0], [xstep, 0], [0, 0]])
        delta_steps.append([[0, 0], [0, 0], [0, -y_up], [0, 0]])
        #  Puts the back-right leg forward
        delta_steps.append([[0, 0], [0, 0], [0, 0], [0, y_up]])
        delta_steps.append([[0, 0], [0, 0], [0, 0], [xstep, 0]])
        delta_steps.append([[0, 0], [0, 0], [0, 0], [0, -y_up]])
        # Offset the body
        delta_steps.append([[x_offset, 0], [x_offset, 0], [x_offset, 0], [x_offset, 0]])
        #  Puts the front-left leg forward
        delta_steps.append([[0, y_up], [0, 0], [0, 0], [0, 0]])
        delta_steps.append([[xstep, 0], [0, 0], [0, 0], [0, 0]])
        delta_steps.append([[0, -y_up], [0, 0], [0, 0], [0, 0]])
        #   Puts the front-right leg forward
        delta_steps.append([[0, 0], [0, y_up], [0, 0], [0, 0]])
        delta_steps.append([[0, 0], [xstep, 0], [0, 0], [0, 0]])
        delta_steps.append([[0, 0], [0, -y_up], [0, 0], [0, 0]])
        delta_steps.append([[-x_offset, 0], [-x_offset, 0], [-x_offset, 0], [-x_offset, 0]])
        delta_steps.append([[-xstep, 0], [-xstep, 0], [-xstep, 0], [-xstep, 0]])

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
            # change vector base for the inverse_kinematic function to get angles at joints
            angle0, angle1 = inverse_kinematic(leg[1], leg[0], 70, 100)
            angle_step.append([angle0, angle1])
        angle_steps.append(angle_step)

    return angle_steps

def stand_up_move():
    """
    @return: array of positions of 2 joints for each of the 4 feet from walk sequence
    """
    x = 80
    y = 150
    delta_steps = []
    delta_steps.append([[0, x], [0, x], [0, x], [0, x]])
    delta_steps.append([[0, y], [0, y], [0, y], [0, y]])

    return delta_steps