def is_sudoku_board_valid(board):
    if not are_characters_valid(board):
        return False

    if not are_rows_valid(board):
        return False

    if not are_cols_valid(board):
        return False

    if not are_boxes_valid(board):
        return False

    return True


def are_characters_valid(board):
    for row in board:
        for cell in row:
            if cell not in "123456789.":
                return False
    return True


def are_rows_valid(board):
    for row in board:
        if has_duplicates(row):
            return False
    return True


def are_cols_valid(board):
    for col_index in range(len(board)):
        col = extract_col(board, col_index)
        if has_duplicates(col):
            return False
    return True


def extract_col(board, col_index):
    """Extract column col_index from board."""
    return [board[row_index][col_index] for row_index in range(len(board))]


def are_boxes_valid(board):
    box_size = 3
    for row_index in range(0, len(board), box_size):
        for col_index in range(0, len(board), box_size):
            box = extract_box(board, row_index, col_index, box_size)
            if has_duplicates(box):
                return False
    return True


def extract_box(board, row_index, col_index, box_size=3):
    """Extract box starting at (row_index, col_index)."""
    rows = board[row_index : row_index + box_size]
    items = []
    for row in rows:
        items.extend(row[col_index : col_index + box_size])
    return items


def has_duplicates(items):
    """Check whether there are duplicate items in a given list."""
    # if set of items is less than items, then some items are not unique
    filtered_items = filter_items(items)
    return len(set(filtered_items)) != len(filtered_items)

    ## alternative solution
    # filtered_items = filter_items(items)
    # for (index1, element1) in enumerate(filtered_items):
    #    for (index2, element2) in enumerate(filtered_items):
    #        if index1 != index2:
    #            if element1 == element2:
    #                return True
    # return False


def filter_items(items):
    """Remove blank cells."""
    return [item for item in items if item != "."]
