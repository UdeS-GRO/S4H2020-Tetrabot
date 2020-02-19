from display import AnimationFrame
from gui import Gui
# from servo import move as write_to_servos
from positions import get_positions_template, smooth_steps


class Controler:
    def __init__(self):
        self.step_index = 0
        self.resolution = 5
        self.period = 1000
        self.delay = int(self.period / self.resolution)

        self.steps = smooth_steps(get_positions_template(), self.resolution)
        self.gui = Gui()

    def main_loop(self):
        run = self.gui.is_running()
        if run:
            step = self.steps[self.step_index]
            self.gui.animate_step(step)
            # write_to_servos(step)

            self.step_index += 1

            if self.step_index >= len(self.steps):
                self.step_index = 0
                # TODO self.redraw(True, draw_trajectory)
            else:
                pass
                # TODO self.redraw(False, draw_trajectory)
        else:
            self.step_index = 0

        self.gui.root.after(self.delay, self.main_loop)


if __name__ == "__main__":
    controler = Controler()
    controler.main_loop()
    controler.gui.root.mainloop()
