__author__ = 'Paola'
from classes import weather as weather
from classes import plants as plants
from time import sleep as sleep

list = []

for x in range(0,3):
    list.append(plants.BasePlant())


def start_simulation():
    y = weather.Weather()
    current_weather = y.generate_weather()
    for x in list:
        if x.live(current_weather):
            x.output_stats()

        else:
            list.remove(x)


while True:
    start_simulation()