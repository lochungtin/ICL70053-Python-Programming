from random import choice, choices, randint

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
    return {
        "name": choice(read_name_file("robot_project/robot_names.txt")),
        "id": base_id + robot_index,
        "position": (randint(0, grid_size - 1), randint(0, grid_size - 1)),
        "direction": randint(0, 3),
    }


def run_simulation(robot, destination):
    """Start robot navigation simulation.

    Args:
        robot (dict[str, any]): robot current data
        destination (Tuple[int, int]): robot's destination
    """
    print("\n{} is searching for its drink.".format(robot["name"]))

    while robot["position"] != destination:
        if navigate(robot):
            print("Moving one step foward.")
            print_location_data(robot)
        else:
            print("I have a wall in front of me!\nTurning 90 degrees clockwise.")
            rotate_robot(robot)

    print("I am drinking Ribena! I am happy!")


def print_robot_greeting(robot):
    """Print geeting message

    Args:
        robot (dict[str, any]): robot current data
    """
    print("Hello. My name is {}. My ID is {}.".format(robot["name"], robot["id"]))


def navigate(robot):
    """Attempt to move robot forward.

    Args:
        robot (dict[str, any]): robot current data

    Returns:
        bool: whether the robot has moved
    """
    prev_row, prev_col = robot["position"]
    row, col = robot["position"]

    if robot["direction"] < 2:
        row = regulate_position(prev_row + (2 * robot["direction"] - 1), prev_row)
    else:
        col = regulate_position(prev_col + (2 * robot["direction"] - 5), prev_col)

    robot["position"] = (row, col)

    return prev_row != row or prev_col != col


def regulate_position(new_value, old_value):
    """Check if new position is within the grid boundaries.

    Args:
        new_value (int): new position value
        old_value (int): old position value

    Returns:
        int: valid position value
    """
    if new_value < 0 or new_value >= grid_size:
        return old_value
    return new_value


def print_location_data(robot):
    """Print the location data

    Args:
        robot (dict[str, any]): robot current data
    """
    print(
        "My current location is {}, facing {}".format(
            robot["position"], directions[robot["direction"]]
        )
    )


def rotate_robot(robot):
    """Rotates the robot 90 degrees clockwise.

    Args:
        robot (dict[str, any]): robot current data
    """
    robot["direction"] = clockwise_rotation_table[robot["direction"]]


robots = 3
robot_data = []
for index, destination in enumerate(choices(destinations, k=robots)):
    robot = setup_robot(grid_size, index)
    robot_data.append((robot, destination))
    print_robot_greeting(robot)

for data in robot_data:
    robot, destination = data
    run_simulation(robot, destination)
