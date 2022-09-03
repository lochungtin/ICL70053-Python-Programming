from random import choices

from drinkfactory import DrinkFactory
from grid import Grid
from robotfactory import RobotFactory

if __name__ == "__main__":
    simulation_counter = 3

    grid = Grid(10)

    for (drink, position) in DrinkFactory(grid.size).create_drinks(simulation_counter):
        grid.add_drink(drink, position)

    for robot in RobotFactory(grid.size).create_robots(simulation_counter):
        robot.set_grid(grid)
        robot.navigate_to_drink()
