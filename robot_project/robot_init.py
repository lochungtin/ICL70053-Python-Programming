from random import choice, randint

from robot import Robot

base_id = 1000


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
        base_id + robot_index + 1,
        (randint(0, grid_size - 1), randint(0, grid_size - 1)),
        randint(0, 3),
        grid_size,
    )
