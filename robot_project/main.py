from random import randint

# grid size limit (square)
grid_size = 10

# robot current coordinates
row_index = randint(0, grid_size - 1)
col_index = randint(0, grid_size - 1)

# quadrant indentifiers
quadrant_prompt = ["top left", "top right", "bottom left", "bottom right"]
# robot current quadrant index
quadrant_index = 0

# direction indentifiers
direction_prompt = ["North", "South", "West", "East"]
# direction (simple) to number conversion table
direction_indices = {"n": 0, "s": 1, "w": 2, "e": 3}
# robot current direction
direction = randint(0, 3)


def regulatePosition(value):
    """
    Regulate robot position w.r.t to the grid size limit.
    Returns the regulated grid size.
    """
    if value < 0:
        return 0

    if value > grid_size - 1:
        return grid_size - 1

    return value


def updateQuadrantIndex():
    """Recalculate and update robot quadrant index value"""
    global quadrant_index

    # branchless if statement numeric hack
    quadrant_index = (row_index > 4) * 2 + (col_index > 4)


def printLocation():
    """Print location information"""
    print(
        "My current location is ({}, {}). I am in the {} quadrant".format(
            row_index, col_index, quadrant_prompt[quadrant_index]
        )
    )


def move():
    """Update robot location by 1 step"""
    global row_index, col_index

    if direction < 2:
        # branchless if statement numeric hack
        # if direction == 0, row_index -= 1, else row_index += 1
        row_index = regulatePosition(row_index + (2 * direction - 1))
    else:
        # branchless if statement numeric hack
        # if direction == 2, col_index -= 1, else col_index += 1
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
