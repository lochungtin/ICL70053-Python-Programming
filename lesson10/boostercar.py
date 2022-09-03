from car import BoosterCar
from wheel import Wheel

wheels = [Wheel(38, 0.5)] * 4
booster_car = BoosterCar("Super Sonic", 2021, True, wheels, boost=1.2)

booster_car.accelerate(20)
print(booster_car.speed)

booster_car.accelerate(10)
print(booster_car.speed)

booster_car.decelerate(10)
print(booster_car.speed)
