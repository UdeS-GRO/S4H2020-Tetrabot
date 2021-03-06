import math
from tkinter import *

# Sets the robot's physical parameters (this can change with your CAD)
legs = []
thigh_length = 100
tibia_length = 100
offset_x = 225
offset_y = 100

# The window where the animation is displayed


class AnimationCanvas:

    def __init__(self, canvas):
        """
        :param canvas: window for animation visualization
        :param offset_3d_x: x offset for 3D visualization
        :offset_3d_y: y offset for 3D visualization
        """

        self.canvas = canvas
        self.offset_3d_x = 0
        self.offset_3d_y = 0
        self.init_ui()

    def init_ui(self):

        index = 0

        for i in range(2):
            for j in range(2):
                leg = Leg(offset_x + 200 * i - self.offset_3d_x * j, offset_y + self.offset_3d_y * j, thigh_length, 0,
                          tibia_length, 0, j)
                legs.append(leg)
                index += 1

        self.canvas.pack(fill=BOTH, expand=1)

    # Displays the steps with the trajectory and the step of each joints (with the option of drawing in 3d)
    def display_step(self, step, draw_trajectory, draw_3d):
        """
        :param step: steps array
        :param draw_trajectory: boolean option for trajectory visualization
        :param draw_3d: boolean option for 3D visualization
        """

        for i, leg_angles in enumerate(step):
            legs[i].set_angles(leg_angles[0], leg_angles[1])

        # Delete tags before the redraw (display trajectory 'foot' or not 'foot')
        if draw_trajectory:
            self.canvas.delete('body', 'shoulder', 'thigh',
                               'tibia', 'knee', 'foot', 'ground')
        else:
            self.canvas.delete('body', 'shoulder', 'thigh', 'tibia',
                               'knee', 'foot', 'foot_trajectory', 'ground')

        # Shows the legs on the FrameCanvas
        for leg in legs:
            leg.show(self.canvas)
        index = 0
        for i in range(2):
            for j in range(2):
                leg = legs[index]
                leg.posx0 = offset_x + 200 * (1 - i) - self.offset_3d_x * j
                leg.posy0 = offset_y + self.offset_3d_y * j
                index += 1

        # Ground
        off_y = 0
        self.canvas.create_line(0, offset_y + thigh_length + tibia_length / 2 + off_y, 1000,
                                offset_y + thigh_length + tibia_length / 2 + off_y, tags='ground')

        # 2D <--> 3D
        if draw_3d:
            self.canvas.create_line(legs[0].posx0, legs[0].posy0, legs[1].posx0, legs[1].posy0, legs[3].posx0,
                                    legs[3].posy0, legs[2].posx0, legs[2].posy0, legs[2].posx0, legs[2].posy0,
                                    legs[0].posx0, legs[0].posy0, tags='body')
            self.offset_3d_x = 40
            self.offset_3d_y = 40
        else:
            self.canvas.create_line(
                legs[2].posx0, legs[2].posy0, legs[0].posx0, legs[0].posy0, tags='body')
            self.offset_3d_x = 0
            self.offset_3d_y = 0

        self.canvas.pack(fill=BOTH, expand=1, padx=10)


class Leg:
    """
    Class for each joint animation of the robot
    """

    def __init__(self, x, y, length1, angle1, length2, angle2, color):
        """
        :param posx0 and posy0: initial positions of X and Y
        :param length1 and length2: Physical lengths of the joints (J1,J2) of the robot
        :param angle1 and angle2: Angles of each joints (J1,J2) of the robot
        """
        self.posx0 = x
        self.posy0 = y
        self.length1 = length1
        self.angle1 = angle1
        self.length2 = length2
        self.angle2 = angle2
        if color == 1:
            self.color = 'purple'
        else:
            self.color = 'darkorchid'

        self.width = 10
        self.width_dot = .75*self.width
        self.width_trajectory = 2

        # set_angles of each joint
    def set_angles(self, angle1, angle2):
        self.angle1 = angle1
        self.angle2 = angle2

    # displays the legs on the canvas with the draw_trajectory
    def show(self, canvas):
        """
        :param canvas: window for animation visualization
        :param draw_trajectory: the mouvement to display on the canvas
        """
        posx1 = self.posx0 + self.length1 * math.sin(self.angle1)
        posy1 = self.posy0 + self.length1 * math.cos(self.angle1)

        posx2 = posx1 + self.length2 * math.sin(self.angle1 + self.angle2)
        posy2 = posy1 + self.length2 * math.cos(self.angle1 + self.angle2)

        # Line of the thigh
        canvas.create_line(self.posx0, self.posy0, posx1, posy1,
                           width=self.width, fill=self.color, tags='thigh')

        # Line of the tibia
        canvas.create_line(posx1, posy1, posx2, posy2,
                           width=self.width, fill=self.color, tags='tibia')

        # Shoulder points
        canvas.create_oval(self.posx0 - self.width_dot, self.posy0 - self.width_dot, self.posx0 + self.width_dot,
                           self.posy0 + self.width_dot, fill='black', tags='shoulder')

        # Knee points
        canvas.create_oval(posx1 - self.width_dot, posy1 - self.width_dot, posx1 + self.width_dot,
                           posy1 + self.width_dot, fill='black', tags='knee')

        # Foot points
        canvas.create_oval(posx2 - self.width_dot, posy2 - self.width_dot, posx2 + self.width_dot,
                           posy2 + self.width_dot, fill='black', tags='foot')

        # Foot trajectory
        canvas.create_oval(posx2 - self.width_trajectory, posy2 - self.width_trajectory, posx2 + self.width_trajectory,
                           posy2 + self.width_trajectory, fill='black', tags='foot_trajectory')
