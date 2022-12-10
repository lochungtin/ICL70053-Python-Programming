def get_winner(board):
    n = len(board)

    winner = check_row_winner(board)
    if winner is not None:
        return winner
        
    winner = check_col_winner(board)
    if winner is not None:
        return winner

    winner = check_diagonal_winner(board)
    if winner is not None:
        return winner
        
    is_game_complete = are_all_cells_occupied(board)
    if is_game_complete:
        return "draw"
    else:
        return None


def check_row_winner(board):
    """ Check rows for all "x", all "o", or neither (return None). """
    for row in board:
        x_wins = all([cell=="x" for cell in row])
        if x_wins:
            return "x"
 
        o_wins = all([cell=="o" for cell in row])
        if o_wins:
            return "o"
    
    return None


def check_col_winner(board):
    """ Check columns for all "x", all "o", or neither (return None). """
    for c in range(len(board)):
        x_wins = all([board[r][c]=="x" for r in range(len(board))]) 
        if x_wins:
            print(3)
            return "x"

        o_wins = all([board[r][c]=="o" for r in range(len(board))])
        if o_wins:
            print(4)
            return "o"
            
    return None
    
    
def check_diagonal_winner(board):
    """ Check diagonal for all "x", all "o", or neither (return None). """
    x_wins = all([board[i][i]=="x" for i in range(len(board))])
    if x_wins:
        return "x"

    o_wins = all([board[i][i]=="o" for i in range(len(board))])
    if o_wins:
        return "o"
        
    return None
    
    
def check_counterdiagonal_winner(board):
    """ Check counterdiagonal for all "x", all "o", or neither (return None). """
    n = len(board)
    
    x_wins = all([board[i][n-i-1]=="x" for i in range(n)])
    if x_wins:
        return "x"

    o_wins = all([board[i][n-i-1]=="o" for i in range(n)])
    if o_wins:
        return "o"
        
    return None
    

def are_all_cells_occupied(board):
    """ Check whether all cells are occupied """
    n = len(board)
    return all([board[r][c] in ["o", "x"] for r in range(n) for c in range(n)])
    
    ## alternative solution
    #n = len(board)
    #return not any([board[r][c]==" " for r in range(n) for c in range(n)])
    
    ## alternative solution
    #n = len(board)
    #if any([board[r][c]==" " for r in range(n) for c in range(n)]): 
    #    return False
    #else:
    #    return True
