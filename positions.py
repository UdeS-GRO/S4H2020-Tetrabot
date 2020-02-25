# get p
def get_positions_from_walk_sequence():
    """
     @return: array of delta positions of 2 joints for each of the 4 feet from walk sequence
     """

    delta_steps = []
    delta_steps.append([[0, -100], [0, -100], [0, -100], [0, -100]])
    delta_steps.append([[0, 0], [0, 0], [0, 0], [0, 40]])

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
