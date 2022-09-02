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
        grid_size (int): The size of the grid.
        robot_index (int): The index of the current robot

    Returns:
        str: Robot name
        int: Robot ID
        Tuple[int, int]: Robot's position
        str: Robot's direction ("n", "s", "w", or "e")
    """
    return (
        choice(read_name_file("robot_project/robot_names.txt")),
        base_id + robot_index,
        (randint(0, grid_size - 1), randint(0, grid_size - 1)),
        randint(0, 3),
    )


def run_simulation(name, position, direction, destination):
    """Start robot navigation simulation.

    Args:
        name (str): name of the robot
        position (Tuple[int, int]): robot's starting position
        direction (int): robot's starting direction
        destination (Tuple[int, int]): robot's destination
    """
    print("\n{} is searching for its drink.".format(name))

    while position != destination:
        position, moved = navigate(position, direction)

        if moved:
            print("Moving one step foward.")
            print_location_data(position, direction)
        else:
            print("I have a wall in front of me!\nTurning 90 degrees clockwise.")
            direction = rotate_robot(direction)

    print("I am drinking Ribena! I am happy!")


def print_robot_greeting(name, id):
    """Print geeting message

    Args:
        name (str): Name of the robot
        id (int): ID of the robot
    """
    print("Hello. My name is {}. My ID is {}.".format(name, id))


def navigate(position, direction):
    """Attempt to move robot forward.

    Args:
        position (Tuple[int, int]): robot's current position
        direction (int): direction of the robot

    Returns:
        Tuple[int, int]: robot's new position
        bool: whether the robot has moved
    """
    prev_row, prev_col = position
    row, col = position

    if direction < 2:
        row = regulate_position(prev_row + (2 * direction - 1), prev_row)
    else:
        col = regulate_position(prev_col + (2 * direction - 5), prev_col)

    return (row, col), prev_row != row or prev_col != col


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


def print_location_data(position, direction):
    """Print the location data

    Args:
        position (Tuple[int, int]): robot's position
        direction (int): direction of the robot
    """
    print(
        "My current location is {}, facing {}".format(position, directions[direction])
    )


def rotate_robot(direction):
    """Rotates the robot 90 degrees clockwise.

    Args:
        direction (int): current robot direction

    Returns:
        int: new robot direction after rotation

    """
    return clockwise_rotation_table[direction]


robots = 3
robot_data = []
for index, destination in enumerate(choices(destinations, k=robots)):
    name, id, position, direction = setup_robot(grid_size, index)
    robot_data.append((name, position, direction, destination))
    print_robot_greeting(name, id)

for data in robot_data:
    name, position, direction, destination = data
    run_simulation(name, position, direction, destination)
