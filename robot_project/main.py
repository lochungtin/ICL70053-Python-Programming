from random import randint

# grid size limit (square)
grid_size = 10

# robot current coordinates
row_index = randint(0, grid_size - 1)
col_index = randint(0, grid_size - 1)
prev_row_index = row_index
prev_col_index = col_index

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

# turning table
clockwise_turning_table = {0: 3, 3: 1, 1: 2, 2: 0}


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
        "My current location is ({}, {}), facing {}.".format(
            row_index, col_index, direction_prompt[direction]
        )
    )


def move():
    """Update robot location by 1 step"""
    global row_index, col_index, prev_row_index, prev_col_index

    if direction < 2:
        # branchless if statement numeric hack
        # if direction == 0, row_index -= 1, else row_index += 1
        prev_row_index = row_index
        row_index = regulatePosition(row_index + (2 * direction - 1))
    else:
        # branchless if statement numeric hack
        # if direction == 2, col_index -= 1, else col_index += 1
        prev_col_index = col_index
        col_index = regulatePosition(col_index + (2 * direction - 5))

    if prev_row_index == row_index and prev_col_index == col_index:
        print("I have a wall in front of me!")
        return False
    else:
        updateQuadrantIndex()

        print("Moving one step forward.")
        printLocation()

        return True


def turnClockwise():
    global direction

    direction = clockwise_turning_table[direction]

    print("Turning 90 degrees clockwise.")
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

reached = False
while True:
    while move():
        if row_index == grid_size - 1 and col_index == grid_size - 1:
            reached = True
            break

    if reached:
        break

    turnClockwise()

print("I am drinking Ribena! I am happy!")
