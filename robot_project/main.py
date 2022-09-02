from random import randint

grid_size = 10

directions = ["North", "South", "West", "East"]
clockwise_rotation_table = {0: 3, 3: 1, 1: 2, 2: 0}

dest_row = 9
dest_col = 9


def run_simulation(grid_size=10):
    """Start robot navigation simulation.

    Args:
        grid_size (int): The size of the grid. Defaults to 10.
    """
    name, id, row, col, direction = setup_robot(grid_size)
    print_robot_greeting(name, id)

    while not at_destination(row, col):
        row, col, moved = navigate(row, col, direction)

        if moved:
            print("Moving one step foward.")
            print_location_data(row, col, direction)
        else:
            print("I have a wall in front of me!\nTurning 90 degrees clockwise.")
            direction = rotate_robot(direction)

    print("I am drinking Ribena! I am happy!")


def setup_robot(grid_size):
    """Initialise the robot name, ID, and initial position and direction.

    Args:
        grid_size (int): The size of the grid.

    Returns:
        str: Robot name
        int: Robot ID
        int: Robot's row coordinate
        int: Robot's column coordinate
        str: Robot's direction ("n", "s", "w", or "e")
    """
    return (
        input("What is the name of the robot? "),
        1000,
        randint(0, grid_size - 1),
        randint(0, grid_size - 1),
        randint(0, 3),
    )


def print_robot_greeting(name, id):
    """Print geeting message

    Args:
        name (str): Name of the robot
        id (int): ID of the robot
    """
    print("Hello. My name is {}. My ID is {}.".format(name, id))


def at_destination(row, col):
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


run_simulation(grid_size)
