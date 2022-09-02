from random import choice, choices

from drink import Drink


class DrinkFactory:
    def __init__(self, grid_size):
        self.counter = 0
        edge = grid_size - 1

        self.spawn_locations = [(0, 0), (0, edge), (edge, 0), (edge, edge)]

    def create_drink(self):
        drink = Drink("Cola", self.counter), choice(self.spawn_locations)
        self.counter += 1
        return drink

    def create_drinks(self, counter):
        drinks = [
            (Drink("Cola", self.counter + index), location)
            for index, location in enumerate(choices(self.spawn_locations, k=counter))
        ]
        self.counter += counter
        return drinks
