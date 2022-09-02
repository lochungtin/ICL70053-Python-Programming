class Car:
    def __init__(
        self, model, year, is_manual, max_passengers=5, speed=0.0, rotation=0.0
    ):
        self.model = model
        self.year = year
        self.is_manual = is_manual
        self.max_passengers = max_passengers
        self.speed = speed
        self.rotation = rotation


personal_car = Car("Honda Civic", 2015, False)
print(personal_car)
print(personal_car.model)
print(personal_car.year)
print(personal_car.is_manual)
print(personal_car.max_passengers)
print(personal_car.speed)
print(personal_car.rotation)
