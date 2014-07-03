__author__ = 'Jose Campos'
from beings import Beings


class BasePlant(Beings):
    def __init__(self):
        self.Weather_min = 10
        self.Weather_max = 40
        self.Max_age = 100

    def live(self,weather):
        self.process_time()
        self.process_weather(weather,True)
        if self.Vitality < 1:
            self.Alive = False

        if self.Alive:
            return True
        else:
            return False




