board1 = [
    ['x','o',' ','o','x'],
    ['x','x','o',' ',' '],
    ['o','o','x',' ',' '],
    [' ','o','o','x','o'],
    [' ',' ',' ',' ','x']
]

board2 = [
    [' ','x',' '],
    ['o','o','o'],
    ['x','x',' ']
]

board3 = [
    ['o','x','o','x'],
    ['o','o','o','x'],
    ['x','x','x','o'],
    ['x','o','x','o']
]

board4 = [
    [' ',' ',' ','o',' ',' ','o'],
    [' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' '],
    ['x',' ','x','x',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' '],
    ['x',' ',' ',' ',' ',' ','o']
]

def print_board(board):
    """ Displays the board in a more visually appealing way
    """
    length = len(board)
    print("+".join(["---"]*length))
    for row in board:
        print(" " + " | ".join([cell for cell in row]))
        print("+".join(["---"]*length))


if __name__ == "__main__":
    print_board(board1)
    print_board(board2)
    print_board(board3)
    print_board(board4)

