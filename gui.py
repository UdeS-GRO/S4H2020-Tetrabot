from tkinter import *
from display import AnimationCanvas


class Gui:
    """
    Class for the Graphics user interface, where the simulation is displayed along with visualization options.
    """
    def __init__(self):
        """
         @param label: label of the window
         @param window_width and window_height : Visualization window size
         @param Buttons : Multiple buttons that the user can set for different visualization (3D, Start, stop)
         """
        self.root = Tk()

        label = Label(self.root, text="TETRABOT PROJECT", font="Helvetica 20")
        label.pack()
        window_width = 800
        window_height = 400

        self.var_draw_trajectory = IntVar()
        self.var_3d = IntVar(value=1)
        self.var_running = IntVar()

        canvas1 = Canvas(self.root, width=window_width, height=window_height, bg='gray')
        self.animation_frame = AnimationCanvas(self.root, canvas1)

        bouton1 = Button(self.root, text='Start').pack(side=LEFT, padx=30, pady=10)
        bouton2 = Button(self.root, text='Stop').pack(side=LEFT, padx=30, pady=10)
        bouton3 = Button(self.root, text="Close", command=self.root.quit).pack(side=RIGHT, padx=30, pady=10)
        bouton4 = Checkbutton(self.root, text="display trajectory", variable=self.var_draw_trajectory).pack(side=RIGHT,
                                                                                                            padx=30,
                                                                                                            pady=10)
        bouton5 = Checkbutton(self.root, text="3D display", variable=self.var_3d).pack(side=RIGHT, padx=30, pady=10)

    def is_running(self):
        return self.var_running

    def animate_step(self, step):
        self.animation_frame.display_step(step, self.var_draw_trajectory.get(), self.var_3d.get())


if __name__ == "__main__":
    gui = Gui()
    gui.root.mainloop()
