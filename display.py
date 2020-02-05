from tkinter import *
from simulation import GUI


class gui_fat:

    def __init__(self):
        self.root = Tk()

        label = Label(self.root, text="TETRABOT PROJECT", font="Helvetica 20")
        label.pack()

        # canvas
        # canvas = Canvas(self.root, width=150, height=220, background='red')
        # ligne1 = canvas.create_line(75, 0, 75, 120)
        # ligne2 = canvas.create_line(0, 60, 150, 60)
        # txt = canvas.create_text(75, 60, text="Cible", font="Arial 16 italic", fill="blue")
        # canvas.pack()

        l = 800
        h = 400
        lt = 100  # l tetrabot

        self.var_draw_trajectory = IntVar()

        canvas1 = Canvas(self.root, width=l, height=h, bg='gray')
        self.gui = GUI(self.root, canvas1)
        # gui = GUI(self.root, width=l, height=h, bg='gray')

        bouton1 = Button(self.root, text='Start').pack(side=LEFT, padx=30, pady=10)
        bouton2 = Button(self.root, text='Stop').pack(side=LEFT, padx=30, pady=10)
        bouton3 = Button(self.root, text="Close", command=self.root.quit).pack(side=RIGHT, padx=30, pady=10)
        bouton4 = Checkbutton(self.root, text="Display trajectory", variable=self.var_draw_trajectory).pack(side=RIGHT, padx=30, pady=10)
        # self.root.after(, self.animate_walk)

        print(self.var_draw_trajectory.get())

    def main_loop(self):
        # print(self.var_draw_trajectory.get())
        delay_ms = self.gui.animate_walk(self.var_draw_trajectory.get())
        self.root.after(delay_ms, self.main_loop)


if __name__ == "__main__":
    gui = gui_fat()
    gui.main_loop()
    gui.root.mainloop()
