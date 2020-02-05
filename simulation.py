# from tkinter import *
#
#  CODE TO ADD SLIDERS
# def main():
#     root = Tk()
#     var = DoubleVar()
#     scale = Scale(root, variable=var)
#     scale.pack(anchor=CENTER)
#
#     # button = Button(root, text="Get Scale Value", command=sel)
#     # button.pack(anchor=CENTER)
#
#     label = Label(root) 
#     label.pack()
#
#     root.mainloop()
#
#
# if __name__ == "__main__":
#     main()
import math
from tkinter import Tk, Canvas, Frame, BOTH


def deg_to_rad(deg):
    return deg * math.pi / 180


legs = []

step_arriere_gauche = [[-40, 80],[-50, 90], [-30, 90],  [-20, 60]]
step_arriere_droite = [[-40, 80], [-40, 80], [-40, 80], [-40, 80]]
step_avant_gauche__ = step_arriere_droite
step_avant_droite__ = step_arriere_droite

animation_steps = [step_arriere_gauche, step_arriere_droite, step_avant_gauche__, step_avant_droite__]
steps_len = min(len(step_arriere_gauche), len(step_arriere_droite), len(step_avant_gauche__), len(step_avant_droite__))

leg_length = 100
tibia_length = 100
offset_x = 200
offset_y = 50


class GUI():

    def __init__(self, fenetre, canvas):
        # super().__init__()
        self.root = fenetre
        self.canvas = canvas

        self.init_ui()
        self.animation_frame = 0
        self.increm = 0
        self.resolution = 10

    def init_ui(self):
        # self.master.title("Lines")
        # self.pack(fill=BOTH, expand=1)


        index = 0
        vs_x = 0
        vs_y = 0
        for i in range(2):
            for j in range(2):
                print(index)
                leg = Leg(offset_x + 200 * i - vs_x * j, offset_y + vs_y * j, leg_length, deg_to_rad(0),
                          tibia_length,
                          deg_to_rad(0), j)
                legs.append(leg)
                index += 1

        self.canvas.pack(fill=BOTH, expand=1)
        # self.canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)

    def redraw(self, delete=False):
        self.canvas.delete("delete")
        if delete:
            self.canvas.delete("all")
        # self.pack(fill=BOTH, expand=1)

        for leg in legs:
            leg.show(self.canvas)
        off_y = 5
        self.canvas.create_line(0, offset_y + leg_length + tibia_length / 2 + off_y, 1000,
                                offset_y + leg_length + tibia_length / 2 + off_y)
        self.canvas.create_line(legs[0].posx0, legs[0].posy0, legs[1].posx0, legs[1].posy0, legs[3].posx0,
                                legs[3].posy0, legs[2].posx0, legs[2].posy0, legs[2].posx0, legs[2].posy0,
                                legs[0].posx0, legs[0].posy0)
        self.canvas.pack(fill=BOTH, expand=1, padx=15)

    def animate_walk(self):
        for i in range(len(animation_steps)):
            step = animation_steps[i]
            angles = step[self.animation_frame]
            angles_to_go = step[(self.animation_frame + 1) % steps_len]
            angle0 = angles[0] + self.increm * ((angles_to_go[0] - angles[0]) / self.resolution)
            angle1 = angles[1] + self.increm * ((angles_to_go[1] - angles[1]) / self.resolution)
            legs[i].set_angles(deg_to_rad(angle0), deg_to_rad(angle1))
            # legs[i].set_angles(deg_to_rad(angles[0]), deg_to_rad(angles[1]))

        self.increm += 1
        if self.increm > self.resolution:
            self.increm = 0
            self.animation_frame += 1

        if self.animation_frame >= steps_len:
            self.animation_frame = 0
            self.redraw(True)
        else:
            self.redraw()

        self.root.after(int(1000 / self.resolution), self.animate_walk)


class Leg:

    def __init__(self, x, y, length1, angle1, length2, angle2, j):
        self.posx0 = x
        self.posy0 = y
        self.length1 = length1
        self.angle1 = angle1
        self.length2 = length2
        self.angle2 = angle2
        if j == 1:
            self.color = "#fb0"
        else:
            self.color = "green"

        self.width = 5

    def set_angles(self, angle1, angle2):
        self.angle1 = angle1
        self.angle2 = angle2

    def show(self, canvas):
        posx1 = self.posx0 + self.length1 * math.sin(self.angle1)
        posy1 = self.posy0 + self.length1 * math.cos(self.angle1)

        posx2 = posx1 + self.length2 * math.sin(self.angle1 + self.angle2)
        posy2 = posy1 + self.length2 * math.cos(self.angle1 + self.angle2)

        canvas.create_line(self.posx0, self.posy0, posx1, posy1, width=self.width, fill=self.color, tags="delete")
        canvas.create_line(posx1, posy1, posx2, posy2, width=self.width, fill=self.color, tags="delete")
        canvas.create_line(posx1 - 1, posy1 - 1, posx1 + 2, posy1 + 2, width=2, fill='black', tags="delete")
        canvas.create_line(posx2 - 1, posy2 - 1, posx2 + 2, posy2 + 2, width=2, fill='black')


# def main():
#     print("main")
#     gui = GUI()
#     root.geometry("800x400+300+300")
#     gui.animate_walk()
#     root.mainloop()


# if __name__ == '__main__':
#     main()
