__author__ = 'Paola'


class Beings:
    def __init__(self):
        self.Vitality = 100
        self.Age = 0
        self.Fertility = True
        self.Energy = 100
        self.Alive = True

    def process_weather(self,weather, isPlant):
        temp = weather[0]
        rain = weather[1]
        sunny = weather[2]
        if temp < self.Weather_min or temp > self.Weather_max:
            self.Vitality -= 5
        if isPlant:
            if rain:
                self.Vitality += 5
            else:
                self.Vitality -= 3
            if sunny:
                self.Energy += 5
            else:
                self.Energy -= 3

    def process_time(self):
        self.Age += 1
        if self.Age > self.Max_age:
            self.Alive = False
        if self.Alive:
            return True
        else:
            return False

    def output_stats(self):
        print self.Age, self.Vitality, self.Energy
