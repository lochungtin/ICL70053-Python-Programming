clockwise_rotation_table = {0: 3, 3: 1, 1: 2, 2: 0}
directions = ["North", "South", "West", "East"]


class Robot:
    def __init__(self, name, idnum, position, direction, grid_size):
        self.name = name
        self.id = idnum
        self.position = position
        self.direction = direction
        self.grid_max = grid_size - 1

    # messages
    def print_greeting_message(self):
        print("Hello. My name is {}. My ID is {}.".format(self.name, self.id))

    def print_location_message(self):
        print(
            "Moving one step foward.\nMy current location is {}, facing {}".format(
                self.position, directions[self.direction]
            )
        )

    def print_starting_message(self):
        print("\n{} is searching for its drink.".format(self.name))

    def print_ending_message(self):
        print("I am drinking Ribena! I am happy!")

    # set destination
    def set_destination(self, destination):
        self.destination = destination

    # status queries
    def is_at_destination(self):
        return self.position == self.destination

    # movement actions
    def move_foward(self):
        prev_row, prev_col = self.position
        row, col = self.position

        if self.direction < 2:
            row = self.regulate_position_value(row + 2 * self.direction - 1)
        else:
            col = self.regulate_position_value(col + 2 * self.direction - 5)

        self.position = (row, col)

        return row != prev_row or col != prev_col

    def turn_right(self):
        self.direction = clockwise_rotation_table[self.direction]

        print("I have a wall in front of me!\nTurning 90 degrees clockwise.")

    # utility functions
    def regulate_position_value(self, value):
        if value < 0:
            return 0
        if value > self.grid_max:
            return self.grid_max

        return value
