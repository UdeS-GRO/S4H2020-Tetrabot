import math
from tkinter import Tk, Canvas, Frame, BOTH
from inverse_kinematics import inverse_kinematic
from positions import get_positions_template


# from servo import init_servos, move as write_to_servos


def deg_to_rad(deg):
    return (deg * math.pi) / 180


def rad_to_deg(rad):
    return (rad * 180) / math.pi


legs = []
leg_length = 100
tibia_length = 100
offset_x = 200
offset_y = 50
vs_x = 40
vs_y = 40


class AnimationFrame:

    def __init__(self, fenetre, canvas):
        # init_servos()
        self.root = fenetre
        self.canvas = canvas
        self.animation_frame = 0

        self.vs_x = 0
        self.vs_y = 0

        self.init_ui()

    def init_ui(self):

        index = 0

        for i in range(2):
            for j in range(2):
                leg = Leg(offset_x + 200 * i - self.vs_x * j, offset_y + self.vs_y * j, leg_length, deg_to_rad(0),
                          tibia_length,
                          deg_to_rad(0), j)
                legs.append(leg)
                index += 1

        self.canvas.pack(fill=BOTH, expand=1)

    def redraw(self, delete_all=False, draw_trajectory=True):
        self.canvas.delete("delete")
        if delete_all:
            self.canvas.delete("all")

        for leg in legs:
            leg.show(self.canvas, draw_trajectory)
        off_y = 5
        index = 0
        for i in range(2):
            for j in range(2):
                leg = legs[index]
                leg.posx0 = offset_x + 200 * (1-i) - self.vs_x * j
                leg.posy0 = offset_y + self.vs_y * j
                index += 1

        self.canvas.create_line(0, offset_y + leg_length + tibia_length / 2 + off_y, 1000,
                                offset_y + leg_length + tibia_length / 2 + off_y)
        self.canvas.create_line(legs[0].posx0, legs[0].posy0, legs[1].posx0, legs[1].posy0, legs[3].posx0,
                                legs[3].posy0, legs[2].posx0, legs[2].posy0, legs[2].posx0, legs[2].posy0,
                                legs[0].posx0, legs[0].posy0)
        self.canvas.pack(fill=BOTH, expand=1, padx=15)

    def display_step(self, step, draw_trajectory, draw_3d):
        if draw_3d:
            self.vs_x = 40
            self.vs_y = 40
        else:
            self.vs_x = 0
            self.vs_y = 0

        for i in range(len(legs)):
            angle0, angle1 = inverse_kinematic(step[i][0], step[i][1], leg_length, tibia_length)
            legs[i].set_angles(angle0, angle1)

        self.redraw(False, draw_trajectory)


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

    def show(self, canvas, draw_trajectory):
        posx1 = self.posx0 + self.length1 * math.cos(self.angle1)
        posy1 = self.posy0 - self.length1 * math.sin(self.angle1)

        posx2 = posx1 + self.length2 * math.cos(self.angle1 + self.angle2)
        posy2 = posy1 - self.length2 * math.sin(self.angle1 + self.angle2)

        canvas.create_line(self.posx0, self.posy0, posx1, posy1, width=self.width, fill=self.color,
                           tags="delete")  # Line thigh
        canvas.create_line(posx1, posy1, posx2, posy2, width=self.width,
                           fill=self.color, tags="delete")  # Line tibia
        canvas.create_line(posx1 - 1, posy1 - 1, posx1 + 2, posy1 + 2, width=2, fill='black',
                           tags="delete")  # Point thigh
        if draw_trajectory:
            canvas.create_line(posx2 - 1, posy2 - 1, posx2 + 2,
                               posy2 + 2, width=2, fill='black')  # Point tibia
        else:
            canvas.create_line(posx2 - 1, posy2 - 1, posx2 + 2, posy2 + 2, width=2, fill='black',
                               tags="delete")  # Point tibia
