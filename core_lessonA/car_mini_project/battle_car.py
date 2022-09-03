from car import BattleCar, Car
from wheel import Wheel

wheels = [Wheel(38, 0.5)] * 4
battle_car = BattleCar("The Terminator", 2020, True, wheels, 5)
opponent_car = Car("Honda Civic", 2015, True, wheels)

opponent_car.accelerate(50)
print(opponent_car.speed)

battle_car.accelerate(40)
print(battle_car.speed)

battle_car.attack(opponent_car)
print(opponent_car.speed)
