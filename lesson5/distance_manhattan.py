def manhattan_distance(x1, y1, x2, y2):
    """Manhattan distance between two points

    Args:
        x1 (int): x coordinate of point 1
        y1 (int): y coordinate of point 1
        x2 (int): x coordinate of point 2
        y2 (int): y coordinate of point 2

    Returns:
        int: manhattan distance of point 1 and 2

    """
    return abs(x1 - x2) + abs(y1 - y2)


def test_manhattan_distance():
    distance = manhattan_distance(1, 1, 2, 2)
    expected = 2
    assert distance == expected, "Test failed. Expected {} but got {}".format(
        expected, distance
    )


test_manhattan_distance()
