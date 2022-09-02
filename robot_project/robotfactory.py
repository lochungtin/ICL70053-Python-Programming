from random import choice, randint

from robot import Robot


class RobotFactory:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.grid_max = grid_size - 1

        self.names = [line.strip() for line in open("robot_project/robot_names.txt")]
        self.counter = 1000

    def create_robot(self):
        robot = Robot(
            self._generate_name(),
            self._generate_id(),
            self._generate_position(),
            self._generate_direction(),
            self.grid_size,
        )
        robot.print_greeting_message()
        return robot

    def create_robots(self, counter):
        return [self.create_robot() for i in range(counter)]

    def _generate_name(self):
        return choice(self.names)

    def _generate_id(self):
        self.counter += 1
        return self.counter

    def _generate_direction(self):
        return choice(range(4))

    def _generate_position(self):
        return (randint(0, self.grid_max), randint(0, self.grid_max))
