class Car:
    def __init__(
        self, model, year, is_manual, wheels, max_passengers=5, speed=0.0, rotation=0.0
    ):
        self.model = model
        self.year = year
        self.is_manual = is_manual
        self.max_passengers = max_passengers
        self.wheels = wheels
        self.speed = speed
        self.rotation = rotation

        self.resistance_factor = 0.5 * sum([wheel.resistance for wheel in self.wheels])

    def accelerate(self, rate=1):
        self.speed += rate - self.resistance_factor

    def decelerate(self, rate=1):
        self.speed = max(self.speed - rate - self.resistance_factor, 0)

    def brake(self):
        self.speed = 0

    def steer(self, angle):
        self.rotation += angle

        if self.rotation > 180:
            self.rotation = 180
        elif self.rotation < -180:
            self.rotation = -180


class BattleCar(Car):
    def __init__(
        self,
        model,
        year,
        is_manual,
        wheels,
        strength,
        max_passengers=5,
        speed=0.0,
        rotation=0.0,
    ):
        super().__init__(
            model, year, is_manual, wheels, max_passengers, speed, rotation
        )
        self.strength = strength

    def attack(self, car):
        car.decelerate(self.strength)


class BoosterCar(Car):
    def __init__(
        self,
        model,
        year,
        is_manual,
        wheels,
        boost,
        max_passengers=5,
        speed=0.0,
        rotation=0.0,
    ):
        super().__init__(
            model, year, is_manual, wheels, max_passengers, speed, rotation
        )
        self.boost = boost

    def accelerate(self, rate=1):
        return super().accelerate(rate * self.boost)


if __name__ == "__main__":
    personal_car = Car("Honda Civic", 2015, False)

    print(personal_car)
    print(personal_car.model)
    print(personal_car.year)
    print(personal_car.is_manual)
    print(personal_car.max_passengers)
    print(personal_car.speed)
    print(personal_car.rotation)
    print()

    personal_car.accelerate()
    print(personal_car.speed)

    personal_car.accelerate(5)
    print(personal_car.speed)

    personal_car.decelerate()
    print(personal_car.speed)

    personal_car.decelerate(20)
    print(personal_car.speed)

    personal_car.accelerate(10)
    print(personal_car.speed)

    personal_car.brake()
    print(personal_car.speed)

    personal_car.steer(30)
    print(personal_car.rotation)

    personal_car.steer(200)
    print(personal_car.rotation)

    personal_car.steer(-200)
    print(personal_car.rotation)

    personal_car.steer(-200)
    print(personal_car.rotation)
