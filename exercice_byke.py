from multiprocessing.sharedctypes import Value


class Vehicule:
    def __init__ (self, speed):
      self.distance = 0
      self.speed = speed
    def  ride (self, duration):
        travel = self.speed * duration
        self.distance += travel
        return self.distance

class Bike (Vehicule):
    def __init__(self):
       super().__init__(15)

class Car (Vehicule):
    def __init__ (self):
        super().__init__(100)
        self.fuel=100
        self.consumption = 0.05
    def ride(self, duration):
       travel= duration *self.speed
       travel_max = self.fuel/self.consumption
       travel = min (travel, travel_max)
       self.distance += travel
       self.fuel -= travel * self.consumption
    

b= Bike()
c= Car()
d= c.ride(25)
print(c.distance)
print (c.fuel)


    
