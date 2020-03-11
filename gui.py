from tkinter import *
from display import AnimationCanvas


class Gui:
    """
    Class for the Graphics user interface, where the simulation is displayed along with visualization options.
    """
    def __init__(self):
        """
        @param Label: label of the window
        @param window_width and window_height : Visualization window size
        @param Buttons : Multiple buttons that the user can set for different actions (Standing, Run, Stop)
        @param Checkbuttons : Multiple checkbuttons that the user can set for different visualizations (3D, Draw_trajectory)
        """
        self.root = Tk()
        self.root.title('GRO-S4-Project')
        self.var_3d = BooleanVar(value=1)
        self.var_draw_trajectory = BooleanVar()
        self.var_running = BooleanVar(value=0)

        window_width = 600
        window_height = 400

        def click_run():
            self.var_running.set(1)

        def click_stop():
            self.var_running.set(0)

        Label(self.root, text='TETRABOT PROJECT', font='Helvetica 28').pack(padx=30, pady=10)

        canvas1 = Canvas(self.root, width=window_width, height=window_height, bg='#C0C0C0')
        self.animation_frame = AnimationCanvas(self.root, canvas1)

        Button(self.root, text='Run', command=click_run).pack(side=LEFT, padx=10, pady=10)
        Button(self.root, text='Stop', command=click_stop).pack(side=LEFT, padx=10, pady=10)
        Button(self.root, text='Close', command=self.root.quit).pack(side=RIGHT, padx=10, pady=10)

        Checkbutton(self.root, text='Draw trajectory', variable=self.var_draw_trajectory).pack(side=RIGHT, padx=10, pady=10)
        Checkbutton(self.root, text='3D visualisation', variable=self.var_3d).pack(side=RIGHT, padx=10, pady=10)

    def is_running(self):
        return self.var_running.get()

    def animate_step(self, step):
        self.animation_frame.display_step(step, self.var_draw_trajectory.get(), self.var_3d.get())