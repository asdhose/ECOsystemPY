__author__ = 'Paola'
from random import randint as random

class Weather:
    def __init__(self):
        self.Temperature = 5
        self. Rain = False
        self.Sunny = False

    def generate_weather(self):
        self.Temperature += random(0,3)
        self.Rain = True if random(1,10) > 5 else False
        self.Sunny= True if random(1,10) > 5 else False
        new_weather = [self.Temperature, self.Rain, self.Sunny]
        return new_weather