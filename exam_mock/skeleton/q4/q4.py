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
    for i in range(l):
        if len(set(board[i][j] for j in range(l))) == 1 and board[i][0] != " ":
            return board[i][0]
        if len(set(board[j][i] for j in range(l))) == 1 and board[0][i] != " ":
            return board[0][i]
    if len(set(board[i][i] for i in range(l))) == 1 and board[0][0] != " ":
        return board[0][0]
    if len(set(board[i][l - i - 1] for i in range(l))) == 1 and board[0][l - 1] != " ":
        return board[0][l - 1]
    if any(map(lambda x: x == " ", [c for r in board for c in r])):
        return None
    return "draw"
