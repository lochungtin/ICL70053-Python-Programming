from q10 import is_sudoku_board_valid

# the following board configurations are provided for testing purposes
# see boards.py if you want to look at them
from boards import (valid_board1,
                    valid_board2,
                    valid_board3,
                    valid_incomplete_board,
                    invalid_row_board, 
                    invalid_column_board,
                    invalid_box_board,
                    invalid_character_board)

# print_board() prints out a visually appealing board
from boards import print_board


def test_valid_board1():
    print_board(valid_board1)
    result = is_sudoku_board_valid(valid_board1)
    print(result)
    assert result == True


def test_valid_board2():
    print_board(valid_board2)
    result = is_sudoku_board_valid(valid_board2)
    print(result)
    assert result == True


def test_valid_board3():
    print_board(valid_board3)
    result = is_sudoku_board_valid(valid_board3)
    print(result)
    assert result == True


def test_valid_board4():
    print_board(valid_incomplete_board)
    result = is_sudoku_board_valid(valid_incomplete_board)
    print(result)
    assert result == True


def test_invalid_characters():
    print_board(invalid_character_board)
    result = is_sudoku_board_valid(invalid_character_board)
    print(result)
    assert result == False
    

def test_invalid_rows():
    print_board(invalid_row_board)
    result = is_sudoku_board_valid(invalid_row_board)
    print(result)
    assert result == False


def test_invalid_cols():
    print_board(invalid_column_board)
    result = is_sudoku_board_valid(invalid_column_board)
    print(result)
    assert result == False


def test_invalid_boxes():
    print_board(invalid_box_board)
    result = is_sudoku_board_valid(invalid_box_board)
    print(result)
    assert result == False


if __name__ == "__main__":
    test_valid_board1()
    test_valid_board2()
    test_valid_board3()
    test_valid_board4()
    test_invalid_characters()
    test_invalid_rows()
    test_invalid_cols()
    test_invalid_boxes()
