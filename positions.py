def set_positions():
    delta_steps = []
    delta_steps.append([[0, 0], [0, 0], [10, 0], [0, 0]])
    delta_steps.append([[0, 0], [0, 0], [0, 0], [0, 10]])
    delta_steps.append([[0, 0], [10, 0], [0, 0], [0, -10]])

    steps = []

    for i, step in enumerate(delta_steps):
        if i == 0:
            steps.append(delta_steps[i])
        else:
            for j, delta in enumerate(step):
                delta_steps[i][j][0] = delta_steps[i][j][0] + \
                    delta_steps[i - 1][j][0]
                delta_steps[i][j][1] = delta_steps[i][j][1] + \
                    delta_steps[i - 1][j][1]
            steps.append(step)
    return steps


if __name__ == "__main__":
    set_positions()
