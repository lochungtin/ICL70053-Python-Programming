from random import choices

from robot_init import setup_robot

grid_size = 10

destinations = [(0, 0), (0, 9), (9, 0), (9, 9)]


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


if __name__ == "__main__":
    robots = 3
    robot_data = []
    for index, destination in enumerate(choices(destinations, k=robots)):
        robot = setup_robot(grid_size, index)
        robot_data.append((robot, destination))
        robot.print_greeting_message()

    for data in robot_data:
        robot, destination = data
        run_simulation(robot, destination)
