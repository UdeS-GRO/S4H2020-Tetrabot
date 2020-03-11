import unittest
import sys

from main import Controler
from gui import Gui
from display import AnimationCanvas, Leg
from inverse_kinematics import inverse_kinematic
from positions import get_positions_from_walk_sequence, get_positions_from_delta_positions, steps_smoother, get_angles_from_positions
from servo import rad_to_deg, format_step_for_servo, init_servos, move

class TestControler(unittest.TestCase):
    pass
class TestGui(unittest.TestCase):
    pass
class TestAC(unittest.TestCase):
    pass
class TestLeg(unittest.TestCase):
    pass
class TestIK(unittest.TestCase):
    pass
class TestGPFWS(unittest.TestCase):
    pass
class TestGPFDP(unittest.TestCase):
    pass
class TestSS(unittest.TestCase):
    pass
class TestGAFP(unittest.TestCase):
    pass
class TestRtD(unittest.TestCase):
    pass
class TestFSFS(unittest.TestCase):
    pass
class TestIS(unittest.TestCase):
    pass
class TestMove(unittest.TestCase):
    pass
if __name__ == '__main__':
    unittest.main()