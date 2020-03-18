from models import Lamp

class LampController:
    def __init__(self):
        self.lamp = Lamp()

    def set_on(self):
        # Change lamp status to ON
        self.lamp.set_on()

    def get_status(self):
        # Returns True if lamp is ON
        return self.lamp.is_on()