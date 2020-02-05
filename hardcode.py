
def get_positions_walk_1():

    #P1 + 80 (Position en y après l'appel de la fonction get_positions_rise)
    p1 = 45 + 80
    step_arriere_gauche = [[0, -p1],[100, -p1]]
    step_arriere_droite = step_arriere_gauche
    step_avant_gauche__ = step_arriere_droite
    step_avant_droite__ = step_arriere_droite

    animation_steps = [step_arriere_gauche, step_arriere_droite, step_avant_gauche__, step_avant_droite__]
    steps_len = min(len(step_arriere_gauche), len(step_arriere_droite), len(step_avant_gauche__), len(step_avant_droite__))

    return animation_steps, steps_len


def get_positions_rise():

    p1 = 45
    step_arriere_gauche = [[0, -p1],[0, -(p1+80)]]
    step_arriere_droite = step_arriere_gauche
    step_avant_gauche__ = step_arriere_droite
    step_avant_droite__ = step_arriere_droite

    animation_steps = [step_arriere_gauche, step_arriere_droite, step_avant_gauche__, step_avant_droite__]
    steps_len = min(len(step_arriere_gauche), len(step_arriere_droite), len(step_avant_gauche__), len(step_avant_droite__))

    return animation_steps, steps_len