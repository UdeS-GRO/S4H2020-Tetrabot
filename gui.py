from tkinter import *
from display import AnimationCanvas


class Gui:
    """
    Class for the Graphics user interface, where the simulation is displayed along with visualization options.
    """
    def __init__(self):
        """
        @param Label: label of the window
        @param Buttons : Multiple buttons that the user can set for different actions (Standing, Run, Stop)
        @param Checkbuttons : Multiple checkbuttons that the user can set for different visualizations (3D, Draw_trajectory)
        @param window_width and window_height : Visualization window size
        """
        self.root = Tk()
        self.root.title('GRO-S4-Project')
        self.var_3d = BooleanVar(value=1)
        self.var_draw_trajectory = BooleanVar()
        self.var_running = BooleanVar(value=0)
        self.var_standing = BooleanVar(value=0)
        self.var_servo_activation = BooleanVar(value=0)

        window_width = 600
        window_height = 400

        def click_stand():
            self.var_standing.set(1)

        def click_run():
            if self.var_standing.get():
                self.var_running.set(1)

        def click_stop():
            self.var_running.set(0)

        Label(self.root, text='TETRABOT PROJECT', font='Helvetica 28').pack(padx=30, pady=10)

        canvas1 = Canvas(self.root, width=window_width, height=window_height, bg='#C0C0C0')
        self.animation_frame = AnimationCanvas(self.root, canvas1)

        Button(self.root, text='Stand Up', command=click_stand).pack(side=LEFT, padx=10, pady=10)
        Button(self.root, text='Run', command=click_run).pack(side=LEFT, padx=10, pady=10)
        Button(self.root, text='Stop', command=click_stop, fg='red').pack(side=LEFT, padx=10, pady=10)
        Button(self.root, text='Close', command=self.root.quit).pack(side=RIGHT, padx=10, pady=10)

        Checkbutton(self.root, text='Rasberry pi', variable=self.var_servo_activation).pack(side=RIGHT, padx=10,
                                                                                               pady=10)
        Checkbutton(self.root, text='Draw trajectory', variable=self.var_draw_trajectory).pack(side=RIGHT, padx=10,
                                                                                               pady=10)
        Checkbutton(self.root, text='3D visualisation', variable=self.var_3d).pack(side=RIGHT, padx=10, pady=10)

    def standing(self):
        return self.var_standing

    def running(self):
        return self.var_running

    def stand(self):
        self.var_standing.set(1)

    def run(self):
        if self.var_standing.get():
            self.var_running.set(1)

    def stop(self):
        self.var_running.set(0)

    def animate_step(self, step):
        self.animation_frame.display_step(step, self.var_draw_trajectory.get(), self.var_3d.get())