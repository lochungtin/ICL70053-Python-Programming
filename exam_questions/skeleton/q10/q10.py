# def isValid(l):
#     nums = []
#     for c in l:
#         if c not in "123456789.":
#             return False
#         if c != ".":
#             nums.append(c)

#     return len(nums) == len(set(nums))

# def is_sudoku_board_valid(board):
#     for i in range(9):
#         if not isValid([board[i][j] for j in range(9)]):
#             return False

#         if not isValid([board[j][i] for j in range(9)]):
#             return False

#         if not isValid(
#             [board[(i // 3) * 3 + j // 3][(i % 3) * 3 + j % 3] for j in range(9)]
#         ):
#             return False

#     return True


def c(l):
    nums = [n for n in l if n in "123456789"]
    return (len(nums) == len(set(nums))) and all(c in "123456789." for c in l)


def is_sudoku_board_valid(board):
    return all(
        c([board[i][j] for j in range(9)])
        and c([board[j][i] for j in range(9)])
        and c([board[(i // 3) * 3 + j // 3][(i % 3) * 3 + j % 3] for j in range(9)])
        for i in range(9)
    )
