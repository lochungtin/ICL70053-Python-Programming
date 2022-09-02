from random import choices

from drinkfactory import DrinkFactory
from robotfactory import RobotFactory


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
    simulation_counter = 3

    robot_factory = RobotFactory(grid_size)
    drink_factory = DrinkFactory(grid_size)

    robots = robot_factory.create_robots(simulation_counter)
    drinks = drink_factory.create_drinks(simulation_counter)

    for [robot, drink] in zip(robots, drinks):
        run_simulation(robot, drink[1])
