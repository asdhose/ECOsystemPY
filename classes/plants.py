__author__ = 'Jose Campos'
from beings import Beings



class BasePlant(Beings):
    def __init__(self):
        self.Weather_min = 10
        self.Weather_max = 40

    def process_weather(self,weather):
        temp = weather[0]
        rain = weather[1]
        sunny = weather[2]
        if temp < self.Weather_min or temp > self.Weather_max:
            self.Vitality -= 5
        if rain:
            self.Vitality += 5
        else:
            self.Vitality -= 3
        if sunny:
            self.Energy += 5
        else:
            self.Energy -= 3







