from random import choices

from robot_project.robotfactory import RobotFactory


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
    grid_size = 10
    destinations = [(0, 0), (0, 9), (9, 0), (9, 9)]

    robot_count = 3
    factory = RobotFactory(grid_size)
    robots = factory.create_robots(robot_count)

    for index, destination in enumerate(choices(destinations, k=robot_count)):
        run_simulation(robots[index], destination)
