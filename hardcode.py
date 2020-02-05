
def get_positions_walk_1():

    step_arriere_gauche = [[0, -200],[50, -150]]
    step_arriere_droite = [[0, -200], [50, -150]]
    step_avant_gauche__ = step_arriere_droite
    step_avant_droite__ = step_arriere_droite

    animation_steps = [step_arriere_gauche, step_arriere_droite, step_avant_gauche__, step_avant_droite__]
    steps_len = min(len(step_arriere_gauche), len(step_arriere_droite), len(step_avant_gauche__), len(step_avant_droite__))

    return animation_steps, steps_len