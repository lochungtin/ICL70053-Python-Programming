class Grid:
    def __init__(self, size):
        self.size = size
        self.drinks = {}

    def add_drink(self, drink, position):
        if position not in self.drinks:
            self.drinks[position] = []

        self.drinks[position].append(drink)

    def has_filled_drink(self, position):
        if position not in self.drinks:
            return False, None

        for drink in self.drinks[position]:
            if not drink.is_empty():
                return True, drink

        return False, None
