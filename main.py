from gui import Gui
from servo import init_servos, move as write_to_servos
from positions import get_positions_from_walk_sequence, steps_smoother, get_angles_from_positions, stand_up_move


# Class to control parameters of the walk sequence and simulation
# period = the period of the simulation loop
# resolution = the resolution for the walk animation
class Controler:
    """
     Class to control parameters of the walk sequence and simulation
     period = the period of the simulation loop
     resolution = the resolution for the walk animation
     """
    def __init__(self):
        """
        @param step_index : the index of the current step in the simulation
        @param resolution : the resolution of the simulation
        @param period : the period of the resolution of the simulation
        @param delay : the pause between each walking sequence
        """
        init_servos()
        self.step_index = 0
        self.resolution = 10
        self.period = 500
        self.delay = int(self.period / self.resolution)
        self.state = 0

        # sets the steps to the desired walk sequence and the resolution
        self.steps = get_angles_from_positions(steps_smoother(stand_up_move(), self.resolution))

        # Inits the GUI for the animation view
        self.gui = Gui()

    # Main loop for the animations and walk sequence of the robot
    def main_loop(self):
        # Checks if the GUI is opened and running (for the simulation)
        stand_up = self.gui.is_standing()
        run = self.gui.is_running()

        if self.state == 0: # Wait command stand_up
            if stand_up:
                if self.step_index >= len(self.steps)/2:
                    self.state = 1
                else:
                    self.step_index += 1

        elif self.state == 1: # Stand_up and wait command run
            if run:
                self.step_index = 0
                self.steps = get_angles_from_positions(steps_smoother(get_positions_from_walk_sequence(), self.resolution))
                self.state = 2

        elif self.state == 2: # Run and wait futur command
            if run:
                if self.step_index >= len(self.steps):
                    self.step_index = 0
                else:
                    self.step_index += 1

        elif self.state == 3: # Futur state
            pass


        step = self.steps[self.step_index]
        self.gui.animate_step(step)
        write_to_servos(step)
        self.gui.root.after(self.delay, self.main_loop)

# Runs the main_loop of the object "controler". (starts the GUI, starts the main_loop)
if __name__ == "__main__":
    controler = Controler()
    controler.main_loop()
    controler.gui.root.mainloop()
