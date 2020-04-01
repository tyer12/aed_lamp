import unittest
from models import ColorLamp, LampArray

class TestColorLamp(unittest.TestCase):
    def setUp(self):
        self.lamp = ColorLamp()
    
    def test_set_color(self):
        self.lamp.set_color('Red')
        self.assertEqual(self.lamp.get_color(), 'Red')

class TestLampArray(unittest.TestCase):
    def setUp(self):
        self.lamp = LampArray()
        self.lamp.lamps.append(ColorLamp())
        self.lamp.lamps.append(ColorLamp())
    
    def test_state_lamps(self):
        self.lamp.state_lamps()

    def test_turn_on(self):
        self.lamp.turn_on()
        self.assertTrue(self.lamp.state_lamps())

    def test_turn_off(self):
        self.lamp.turn_off()
        self.assertFalse(self.lamp.state_lamps())
    

if __name__ == "__main__":
    unittest.main()