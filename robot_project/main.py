from random import choice, choices, randint

from robot import Robot

grid_size = 10

directions = ["North", "South", "West", "East"]
clockwise_rotation_table = {0: 3, 3: 1, 1: 2, 2: 0}

base_id = 1001

destinations = [(0, 0), (0, 9), (9, 0), (9, 9)]


def read_name_file(filename):
    """Read names from robot name file

    Args:
        filename (str): file path

    Returns:
        list(str): list of names
    """
    return [line.strip() for line in open(filename)]


def setup_robot(grid_size, robot_index):
    """Initialise the robot name, ID, and initial position and direction.

    Args:
        grid_size (int): the size of the grid.
        robot_index (int): the index of the current robot

    Returns:
        dict[str, any]: robot data
    """
    return Robot(
        choice(read_name_file("robot_project/robot_names.txt")),
        base_id + robot_index,
        (randint(0, grid_size - 1), randint(0, grid_size - 1)),
        randint(0, 3),
        grid_size,
    )


def run_simulation(robot, destination):
    """Start robot navigation simulation.

    Args:
        robot (Robot): robot current data
        destination (Tuple[int, int]): robot's destination
    """
    robot.print_starting_message()

    robot.set_destination(destination)
    while not robot.is_at_destination():
        if robot.move_foward():
            robot.print_location_message()
        else:
            robot.turn_right()

    robot.print_ending_message()


robots = 3
robot_data = []
for index, destination in enumerate(choices(destinations, k=robots)):
    robot = setup_robot(grid_size, index)
    robot_data.append((robot, destination))
    robot.print_greeting_message()

for data in robot_data:
    robot, destination = data
    run_simulation(robot, destination)
