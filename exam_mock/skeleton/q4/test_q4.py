from q4 import get_winner

# the following board configurations are provided for testing purposes
# see state.py if you want to look at them
from state import board1, board2, board3, board4

# print_board() prints out a visually appealing board
from state import print_board


def test_x_wins():
    print_board(board1)
    winner = get_winner(board1)
    print(winner)
    assert winner == "x"


def test_o_wins():
    print_board(board2)
    winner = get_winner(board2)
    print(winner)
    assert winner == "o"


def test_draw():
    print_board(board3)
    winner = get_winner(board3)
    print(winner)
    assert winner == "draw"


def test_incomplete():
    print_board(board4)
    winner = get_winner(board4)
    print(winner)
    assert winner == None


if __name__ == "__main__":
    test_x_wins()
    test_o_wins()
    test_draw()
    test_incomplete()

