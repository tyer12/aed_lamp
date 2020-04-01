class Lamp:
    def __init__(self):
        # Lamp is off by default
        self.state = False  

    def is_on(self):
        return self.state

    def is_off(self):
        return self.state

    def set_on(self):
        self.state = True

    def set_off(self):
        self.state = False

class ColorLamp(Lamp):
    def __init__(self):
        Lamp.__init__(self)
        self.color = 'white'

    def set_color(self, color):
        #chage the color of the lamp
        self.color = color

    def get_color(self):
        #return the color of the lamp
        return self.color

class LampArray(Lamp):
    def __init__(self):
        self.lamps = []

    def state_lamps(self):
        count_on = 0
        for lamp in self.lamps:
            if lamp.is_on():
                count_on += 1
        return count_on == len(self.lamps)
        # return sum([1 for lamp in self.lamps if lamp.is_on()]) == len(self.lamps)

    def turn_on(self):
        for lamp in self.lamps:
            lamp.set_on()

    def turn_off(self):
        for lamp in self.lamps:
            lamp.set_off()

    
        