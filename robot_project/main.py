from random import randint

grid_size = 10

row_index = randint(0, grid_size - 1)
col_index = randint(0, grid_size - 1)

quadrant_prompt = ["top left", "top right", "bottom left", "bottom right"]
quadrant_index = 0

direction_prompt = ["North", "South", "West", "East"]
direction_indices = {"n": 0, "s": 1, "w": 2, "e": 3}
direction = randint(0, 3)


def regulatePosition(value):
    if value < 0:
        return 0

    if value > grid_size - 1:
        return grid_size - 1

    return value


def updateQuadrantIndex():
    global quadrant_index
    quadrant_index = (row_index > 4) * 2 + (col_index > 4)


def printLocation():
    print(
        "My current location is ({}, {}). I am in the {} quadrant".format(
            row_index, col_index, quadrant_prompt[quadrant_index]
        )
    )


def move():
    global row_index, col_index

    if direction < 2:
        row_index = regulatePosition(row_index + (2 * direction - 1))
    else:
        col_index = regulatePosition(col_index + (2 * direction - 5))

    updateQuadrantIndex()

    print("Moving one step forward.")
    printLocation()


name = input("What is the name of the robot? ")
# row_index = int(input("What is its row coordinate? "))
# col_index = int(input("What is its column coordinate? "))
# direction_input = input("What is its initial direction [n|s|e|w]? ")

# regulate input values
# row_index = regulatePosition(row_index)
# col_index = regulatePosition(col_index)

# if direction_input in direction_indices:
# direction = direction_indices[direction_input]

# calculate quadrant
updateQuadrantIndex()

print("Hello. My name is {}. My ID is 1000.".format(name))
printLocation()

print("I am facing {}.".format(direction_prompt[direction]))

move()
