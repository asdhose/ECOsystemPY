__author__ = 'Paola'
from classes import weather as weather
from classes import plants as plants
from time import sleep as sleep

list = []

for x in range(0,3):
    list.append(plants.BasePlant())


def start_simulation():
    current_weather = weather.Weather.generate_weather()
    for x in list():
        x.live(current_weather)


while True:
    start_simulation()