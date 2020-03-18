class Lamp:
    def __init__(self):
        self.state = False # Lamp is off by default

    def is_on(self):
        return self.state

    def set_on(self):
        self.state = True