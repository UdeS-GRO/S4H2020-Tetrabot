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

class TestIK(unittest.TestCase):
    def test_IK1(self):
        self.test_1 = [22, 22, 70, 100, 1.107, 3.043]
        q1, q2 = inverse_kinematic(self.test_1[0], self.test_1[1], self.test_1[2], self.test_1[3])
        self.assertAlmostEqual(q1, self.test_1[4], 3, 'Wrong q1')
        self.assertAlmostEqual(q2, self.test_1[5], 3, 'Wrong q2')

    def test_IK2(self):
        self.test_2 = [30, 0, 70, 100, 0.000, 3.142]
        q1, q2 = inverse_kinematic(self.test_2[0], self.test_2[1], self.test_2[2], self.test_2[3])
        self.assertAlmostEqual(q1, self.test_2[4], 3, 'Wrong q1')
        self.assertAlmostEqual(q2, self.test_2[5], 3, 'Wrong q2')

class TestPositions(unittest.TestCase):
    def test_GPFWS(self):
        test_pos = get_positions_from_walk_sequence()
        ans_pos = [[[0, -140], [0, -140], [0, -140], [0, -140]], [[0, -120], [0, -120], [0, -160], [0, -160]], [[0, -120], [0, -120], [0, -140], [0, -160]], [[0, -120], [0, -120], [30, -140], [0, -160]], [[0, -120], [0, -120], [30, -160], [0, -160]], [[0, -120], [0, -120], [30, -160], [0, -140]], [[0, -120], [0, -120], [30, -160], [30, -140]], [[0, -120], [0, -120], [30, -160], [30, -160]], [[0, -140], [0, -140], [30, -140], [30, -140]], [[0, -120], [0, -140], [30, -140], [30, -140]], [[50, -120], [0, -140], [30, -140], [30, -140]], [[50, -140], [0, -140], [30, -140], [30, -140]], [[50, -140], [0, -120], [30, -140], [30, -140]], [[50, -140], [50, -120], [30, -140], [30, -140]], [[50, -140], [50, -140], [30, -140], [30, -140]], [[0, -140], [0, -140], [0, -140], [0, -140]]]
        self.assertEqual(test_pos, ans_pos, 'Wrong positions')

    def test_GPFDP(self):
        self.test_steps = [[[-50, 8], [4, 500], [0, 0], [-900, 1]],[[-5, 80], [40, -5], [-90, 100], [0, 0]]]
        self.ans_steps = [[[-50, 8], [4, 500], [0, 0], [-900, 1]], [[-55, 88], [44, 495], [-90, 100], [-900, 1]]]
        get_steps = get_positions_from_delta_positions(self.test_steps)
        self.assertEqual(get_steps, self.ans_steps, 'Wrong steps')

    def test_SS(self):
        self.test_steps = [[[-50, 8], [4, 500], [0, 0], [-900, 1]],[[-5, 80], [40, -5], [-90, 100], [0, 0]]]
        self.ans_steps = [[[-50.0, 8.0], [4.0, 500.0], [0.0, 0.0], [-900.0, 1.0]], [[-45.5, 15.2], [7.6, 449.5], [-9.0, 10.0], [-810.0, 0.9]], [[-41.0, 22.4], [11.2, 399.0], [-18.0, 20.0], [-720.0, 0.8]], [[-36.5, 29.6], [14.8, 348.5], [-27.0, 30.0], [-630.0, 0.7]], [[-32.0, 36.8], [18.4, 298.0], [-36.0, 40.0], [-540.0, 0.6]], [[-27.5, 44.0], [22.0, 247.5], [-45.0, 50.0], [-450.0, 0.5]], [[-23.0, 51.2], [25.6, 197.0], [-54.0, 60.0], [-360.0, 0.3999999999999999]], [[-18.5, 58.4], [29.2, 146.5], [-63.0, 70.0], [-270.0, 0.29999999999999993]], [[-14.0, 65.6], [32.8, 96.0], [-72.0, 80.0], [-180.0, 0.19999999999999996]], [[-9.5, 72.8], [36.4, 45.5], [-81.0, 90.0], [-90.0, 0.09999999999999998]], [[-5.0, 80.0], [40.0, -5.0], [-90.0, 100.0], [0.0, 0.0]], [[-9.5, 72.8], [36.4, 45.5], [-81.0, 90.0], [-90.0, 0.1]], [[-14.0, 65.6], [32.8, 96.0], [-72.0, 80.0], [-180.0, 0.2]], [[-18.5, 58.4], [29.2, 146.5], [-63.0, 70.0], [-270.0, 0.30000000000000004]], [[-23.0, 51.2], [25.6, 197.0], [-54.0, 60.0], [-360.0, 0.4]], [[-27.5, 44.0], [22.0, 247.5], [-45.0, 50.0], [-450.0, 0.5]], [[-32.0, 36.8], [18.4, 298.0], [-36.0, 40.0], [-540.0, 0.6000000000000001]], [[-36.5, 29.6], [14.8, 348.5], [-27.0, 30.0], [-630.0, 0.7000000000000001]], [[-41.0, 22.4], [11.2, 399.0], [-18.0, 20.0], [-720.0, 0.8]], [[-45.5, 15.200000000000003], [7.600000000000001, 449.5], [-9.0, 10.0], [-810.0, 0.9]]]
        get_steps = steps_smoother(self.test_steps, 10)
        for i in range(0,20):
            group4 = get_steps[i]
            ans4 = self.ans_steps[i]
            for j in range(0,4):
                group2 = group4[j]
                ans2 = ans4[j]
                for k in range(0,2):
                    self.assertAlmostEqual(group2[k], ans2[k], 3, 'Wrong steps')

    def test_GAFP(self):
        self.test_steps = []
        self.test_steps.append([[30, 0], [-15, 45], [0, -50], [100, -5]])
        get_angles = get_angles_from_positions(self.test_steps)
        self.ans_angles = [[[0.000, 3.142], [-0.122, 2.699], [-0.381, 2.659], [-1.262, 1.926]]]
        for i in range(0,1):
            group4 = get_angles[i]
            ans4 = self.ans_angles[i]
            for j in range(0, 4):
                group2 = group4[j]
                ans2 = ans4[j]
                for k in range(0, 2):
                    self.assertAlmostEqual(group2[k], ans2[k], 3, 'Wrong angles')

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