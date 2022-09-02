from car import Car
from wheel import Wheel


class Driver:
    def __init__(self, idnum, name):
        self.name = name
        self.id = idnum

    def drive(self, car):
        print("Driver {} is driving a {}".format(self.name, car.model))
        print("Driver {} is accelerating the car".format(self.name))
        car.accelerate(60)
        print("The car's speed is now {}".format(car.speed))


if __name__ == "__main__":
    wheels = [Wheel(38, 0.5)] * 4
    sports_car = Car("Porsche GT2", 2006, True, wheels, 4)
    driver = Driver("F123", "Michael Schumacher")
    driver.drive(sports_car)
