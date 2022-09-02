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
        int: Robot's row coordinate
        int: Robot's column coordinate
        str: Robot's direction ("n", "s", "w", or "e")
    """
    return (
        choice(read_name_file("robot_project/robot_names.txt")),
        base_id + robot_index,
        randint(0, grid_size - 1),
        randint(0, grid_size - 1),
        randint(0, 3),
    )


def run_simulation(name, row, col, direction, dest_row, dest_col):
    """Start robot navigation simulation.

    Args:
        grid_size (int): The size of the grid. Defaults to 10.
    """
    print("\n{} is searching for its drink.".format(name))

    while not at_destination(row, col, dest_row, dest_col):
        row, col, moved = navigate(row, col, direction)

        if moved:
            print("Moving one step foward.")
            print_location_data(row, col, direction)
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


def at_destination(row, col, dest_row, dest_col):
    """Check if the robot is at the destination

    Args:
        row (int): row index of the robot
        col (int): column index of the robot

    Returns:
        bool: if the robot is at the destination
    """
    return row == dest_row and col == dest_col


def navigate(row, col, direction):
    """Attempt to move robot forward.

    Args:
        row (int): row index of the robot
        col (int): column index of the robot
        direction (int): direction of the robot

    Returns:
        int: new row index of the robot
        int: new column index of the robot
        bool: whether the robot has moved
    """
    prev_row, prev_col = row, col

    if direction < 2:
        row = regulate_position(row + (2 * direction - 1), row)
    else:
        col = regulate_position(col + (2 * direction - 5), col)

    return row, col, prev_row != row or prev_col != col


def regulate_position(new_pos, prev_pos):
    """Check if new position is within the grid boundaries.

    Args:
        new_pos (int): new position value
        old_pos (int): old position value

    Returns:
        int: valid position value
    """
    if new_pos < 0 or new_pos >= grid_size:
        return prev_pos
    return new_pos


def print_location_data(row, col, direction):
    """Print the location data

    Args:
        row (int): row index of the robot
        col (int): column index of the robot
        direction (int): direction of the robot
    """
    print(
        "My current location is ({}, {}), facing {}".format(
            row, col, directions[direction]
        )
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
    name, id, row, col, direction = setup_robot(grid_size, index)
    robot_data.append((name, row, col, direction, destination[0], destination[1]))
    print_robot_greeting(name, id)

for data in robot_data:
    name, row, col, direction, dest_row, dest_col = data
    run_simulation(name, row, col, direction, dest_row, dest_col)
