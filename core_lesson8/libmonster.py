FACTOR = 5


class Monster:
    def __init__(self, name="Me", food="cookies"):
        self.name = name
        self.food = food


def spawn_monsters():
    return [
        Monster("Happy", "carrots"),
        Monster("Bashful", "ice-creams"),
        Monster("Wild", "cookies"),
    ]


def calculate_growthrate(adjustment=3):
    return 25 * FACTOR + adjustment
