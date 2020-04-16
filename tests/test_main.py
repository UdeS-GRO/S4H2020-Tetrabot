import unittest
import time
from main import Controler
from gui import Gui
from display import AnimationCanvas, Leg
from inverse_kinematics import inverse_kinematic
from positions import get_positions_from_walk_sequence, get_positions_from_delta_positions, steps_smoother, get_angles_from_positions
# from servo import rad_to_deg, format_step_for_servo, init_servos, move


class TestGui(unittest.TestCase):

    def test_running(self):
        self.gui = Gui()
        self.assertFalse(self.gui.var_running.get(),'Is running')

    def test_standing(self):
        self.gui = Gui()
        self.assertFalse(self.gui.var_standing.get(),'Is standing')

    def test_3d(self):
        self.gui = Gui()
        self.assertTrue(self.gui.var_3d.get(), '3d not active at start-up')

# class TestDisplay(unittest.TestCase):
#     def test_IU(self):
#         self.assertEqual(AnimationCanvas.init_ui(), 1,
#                          "Wrong answer on test #" + i)
#     def test_DS(self):
#         self.assertEqual(AnimationCanvas.display_step(), 1,
#                          "Wrong answer on test #" + i)
#     def test_SA(self):
#         self.assertEqual(Leg.set_angles(), 1,
#                          "Wrong answer on test #" + i)
#     def test_show(self):
#         self.assertEqual(Leg.show(), 1,
#                          "Wrong answer on test #" + i)
#
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
#
# class TestServo(unittest.TestCase):
#     def test_RtD(self):
#         self.assertEqual(rad_to_deg(), 1,
#                         "Wrong answer on test #" + i)
#
#     def test_FSFS(self):
#         self.assertEqual(format_step_for_servo(), 1,
#                         "Wrong answer on test #" + i)
#
#     def test_IS(self):
#         self.assertEqual(init_servos(), 1,
#                         "Wrong answer on test #" + i)
#
#     def test_Move(self):
#         self.assertEqual(move(), 1,
#                         "Wrong answer on test #" + i)

class TestMain(unittest.TestCase):

    def test_not_moving(self):
        self.controler = Controler()
        self.assertFalse(self.controler.gui.var_standing.get(),'The robot can move without command')
        self.assertFalse(self.controler.gui.var_running.get(),'The robot can move without command')

    def test_counter_init(self):
        self.controler = Controler()
        time.sleep(2)
        self.assertFalse(self.controler.step_index,'The step counter increments')


if __name__ == '__main__':
    unittest.main()