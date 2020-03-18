import unittest
from controllers import LampController

class TestLampController(unittest.TestCase):
    def test_set_on(self):
        controller = LampController()
        controller.set_on()
        self.assertTrue(controller.get_status())
    
    def test_test_off(self):
        controller = LampController()
        controller.set_off()
        self.assertFalse(controller.get_status())

if __name__ == "__main__":
    unittest.main()