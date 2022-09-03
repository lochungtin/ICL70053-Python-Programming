from random import choice, randint, random

from robot import LeapingRobot, Robot


class RobotFactory:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.grid_max = grid_size - 1

        self.names = [line.strip() for line in open("robot_project/robot_names.txt")]
        self.counter = 1000

    def create_robot(self):
        name = self._generate_name()
        id = self._generate_id()
        position = self._generate_position()
        direction = self._generate_direction()

        if random() > 0.5:
            robot = Robot(name, id, position, direction, self.grid_size)
        else:
            robot = LeapingRobot(name, id, position, direction, self.grid_size)

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
