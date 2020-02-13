
def get_positions_walk_1():

    step_arriere_gauche = [[10, -185], [10, -185]]
    step_arriere_droite = [[10, -200],[10, -200]]

    step_avant_gauche__ = [[10, -185], [10, -165]]
    step_avant_droite__ = [[10, -185],[10, -185]]

    animation_steps = [step_arriere_gauche, step_arriere_droite, step_avant_gauche__, step_avant_droite__]
    steps_len = min(len(step_arriere_gauche), len(step_arriere_droite), len(step_avant_gauche__), len(step_avant_droite__))

    return animation_steps, steps_len


def get_positions_rise():

    p1 = 60
    step_arriere_gauche = [[0, -170],[0, -120]]
    step_arriere_droite = step_arriere_gauche
    step_avant_gauche__ = step_arriere_droite
    step_avant_droite__ = step_arriere_droite

    animation_steps = [step_arriere_gauche, step_arriere_droite, step_avant_gauche__, step_avant_droite__]
    steps_len = min(len(step_arriere_gauche), len(step_arriere_droite), len(step_avant_gauche__), len(step_avant_droite__))

    return animation_steps, steps_len

def get_positions_fat():

    off_y = 30

    s_init = [[0,-200+off_y]]
    s_end = [[15,-200+off_y]]
    s = [[0,-180+off_y],[15,-170+off_y],[15,-170+off_y]] + s_end
    
    len_s = len(s)

    step_arriere_gauche = s_init  + s + s_end*3*len_s 
    step_arriere_droite = s_init  + s_init*len_s + s + s_end*2*len_s 
    step_avant_gauche__ = s_init  + s_init*2*len_s + s + s_end*len_s 
    step_avant_droite__ = s_init  + s_init*3*len_s  + s

    # print(len(step_arriere_gauche), len(step_arriere_droite), len(step_avant_gauche__), len(step_avant_droite__))

    animation_steps = [step_arriere_gauche, step_avant_gauche__, step_avant_droite__, step_arriere_droite]
    steps_len = min(len(step_arriere_gauche), len(step_arriere_droite), len(step_avant_gauche__), len(step_avant_droite__))

    return animation_steps, steps_len

if __name__=="__main__":
    get_positions_fat()