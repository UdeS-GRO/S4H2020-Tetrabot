from tkinter import *
from simulation import GUI


class gui_fat:

    def __init__(self):
        self.root = Tk()

        label = Label(self.root, text="TETRABOT PROJECT", font="Helvetica 20")
        label.pack()

        l = 800
        h = 400
        lt = 100  # l tetrabot

        self.var_draw_trajectory = IntVar() 
        self.var_3d = IntVar()

        canvas1 = Canvas(self.root, width=l, height=h, bg='gray')
        self.gui = GUI(self.root, canvas1)
        # gui = GUI(self.root, width=l, height=h, bg='gray')

        bouton1 = Button(self.root, text='Start').pack(side=LEFT, padx=30, pady=10)
        bouton2 = Button(self.root, text='Stop').pack(side=LEFT, padx=30, pady=10)
        bouton3 = Button(self.root, text="Close", command=self.root.quit).pack(side=RIGHT, padx=30, pady=10)
        bouton4 = Checkbutton(self.root, text="display trajectory", variable=self.var_draw_trajectory).pack(side=RIGHT, padx=30, pady=10)
        bouton5 = Checkbutton(self.root, text="3D display", variable=self.var_3d).pack(side=RIGHT, padx=30, pady=10)


    def main_loop(self):
        delay_ms = self.gui.animate_walk(self.var_draw_trajectory.get(),self.var_3d.get())
        self.root.after(delay_ms, self.main_loop)


if __name__ == "__main__":
    gui = gui_fat()
    gui.main_loop()
    gui.root.mainloop()
