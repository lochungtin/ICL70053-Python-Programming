# def f(l):
#     return len(set(l)) == 1 and l[0] != " "


# def get_winner(board):
#     s = any(map(lambda x: x == " ", [c for r in board for c in r]))
#     for i in range(len(board)):
#         if f([board[i][j] for j in range(len(board))]):
#             return board[i][0]
#         if f([board[j][i] for j in range(len(board))]):
#             return board[0][i]
#     if f([board[i][i] for i in range(len(board))]):
#         return board[0][0]
#     if f([board[i][len(board) - 1 - i] for i in range(len(board))]):
#         return board[i][len(board) - i]
#     if s:
#         return None
#     return "draw"


def get_winner(board):
    l = len(board)
    s = [set(board[i][i] for i in range(l)), set(board[i][l - i - 1] for i in range(l))]
    s += [set(board[j][i] for j in range(l)) for i in range(l)]
    s += [set(board[i][j] for j in range(l)) for i in range(l)]
    for w in [list(r)[0] for r in s if len(r) == 1 and " " not in r]:
        return w
    if any(map(lambda x: x == " ", [c for r in board for c in r])):
        return None
    return "draw"
