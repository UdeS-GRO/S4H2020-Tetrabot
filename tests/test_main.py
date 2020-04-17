import unittest
import time
from main import Controler
from gui import Gui
from display import AnimationCanvas, Leg
from inverse_kinematics import inverse_kinematic
from positions import get_positions_from_walk_sequence, get_positions_from_delta_positions, steps_smoother, get_angles_from_positions


class TestGui(unittest.TestCase):

    def test_stand_command(self):
        self.gui = Gui()
        self.assertFalse(self.gui.var_standing.get(), 'Is standing')
        self.gui.stand()
        self.assertTrue(self.gui.var_standing.get(), 'Is not standing')


    def test_run_command(self):
        self.gui = Gui()
        self.assertFalse(self.gui.var_running.get(),'Is running at starting')
        self.gui.run()
        self.assertFalse(self.gui.var_running.get(),'Is not standing before running')
        self.gui.stand()
        self.gui.run()
        self.assertTrue(self.gui.var_running.get(),'Is running')

    def test_3d(self):
        self.gui = Gui()
        self.assertTrue(self.gui.var_3d.get(), '3d not active at start-up')

class TestDisplay(unittest.TestCase):

    def test_Leg(self):
        x = 0
        y = 0
        length1 = 50
        angle1 = 90
        length2 = 50
        angle2 = 90
        color = 'red'
        self.leg = Leg(x,y,length1,angle1,length2,angle2,color)
        self.assertGreaterEqual(self.leg.posx0,0,'No x position valid')
        self.assertGreaterEqual(self.leg.posy0, 0, 'No y position valid')
        self.assertGreater(self.leg.length1, 0, 'No length1')
        self.assertTrue(float(self.leg.angle1), 'No valid angle1')
        self.assertGreater(self.leg.length2, 0, 'No length2')
        self.assertTrue(float(self.leg.angle2), 'No valid angle2')

# class TestIK(unittest.TestCase):
#     def test_IK(self):
#         self.test_data = [[5, 5, 45, 45], [55, 55, 15, 15], [0, 0, 0, 0]]
#         self.test_answers = [1, 1, 1]
#         num = 0
#         for test in self.test_data:
#             self.assertEqual(inverse_kinematic(test[0], test[1], test[2], test[3]), self.test_answers[num],
#                             "Wrong answer on test #" + num)
#             num = num+1
#
# class TestPositions(unittest.TestCase):
#     def test_GPFWS(self):
#         self.assertEqual(get_positions_from_walk_sequence(), 1,
#                         "Wrong answer on test #" + i)
#
#     def test_GPFDP(self):
#         self.assertEqual(get_positions_from_delta_positions(), 1,
#                         "Wrong answer on test #" + i)
#
#     def test_SS(self):
#         self.assertEqual(steps_smoother(), 1,
#                         "Wrong answer on test #" + i)
#
#     def test_GAFP(self):
#         self.assertEqual(get_angles_from_positions(), 1,
#                         "Wrong answer on test #" + i)


class TestMain(unittest.TestCase):

    def test_not_moving(self):
        self.controler = Controler()
        self.controler.main_loop()
        self.assertFalse(self.controler.gui.var_standing.get(),'The robot can move without command')
        self.assertFalse(self.controler.gui.var_running.get(),'The robot can move without command')

    def test_counter_init(self):
        self.controler = Controler()
        self.controler.main_loop()
        time.sleep(1)
        self.assertFalse(self.controler.step_index,'The step counter increments')

    def test_overall(self):
        self.controler = Controler()
        self.controler.main_loop()
        self.assertEqual(self.controler.state, 0, 'State 0')
        self.controler.gui.stand()
        self.controler.gui.run()
        time.sleep(2)
        # self.assertEqual(self.controler.state, 0, 'State 1') # problem


if __name__ == '__main__':
    unittest.main()