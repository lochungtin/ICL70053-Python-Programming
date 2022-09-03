from random import choices

from drinkfactory import DrinkFactory
from grid import Grid
from robotfactory import RobotFactory

if __name__ == "__main__":
    simulation_counter = 3

    grid = Grid(10)

    drinks = DrinkFactory(grid.size).create_drinks(simulation_counter)
    for (drink, position) in drinks:
        grid.add_drink(drink, position)

    robots = RobotFactory(grid.size).create_robots(simulation_counter)
    for robot in robots:
        robot.navigate_to_drink(grid)
