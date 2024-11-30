class lamp:
    def __init__(self, wattage:int, consumption:int, life:int):
        self.wattage = wattage
        self.consumption = consumption
        self.life = life

    def __str__(self):
        return f'Мощность: {self.wattage} \nПотребление: {self.consumption} \nСрок службы: {self.life}'

    def burnout(self, usage:int):
        return round(self.life/usage, 2)

    def ratio(self):
        return self.wattage/self.consumption

class spotlight(lamp):
    def __init__(self, state:bool):
        self.state = state

    def change_state(self):
        self.state = not self.state
        return self.state

class daylight(lamp):
    def __init__(self, brightness=0):
        self.brightness = brightness
    
    def increase_brightness(self, percentage):
        self.brightness += percentage
        if self.brightness > 100: self.brightness = 100
        return self.brightness

    def decrease_brightness(self, percentage):
        self.brightness -= percentage
        if self.brightness < 0: self.brightness = 0
        return self.brightness


