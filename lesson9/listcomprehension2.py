numbers = [[1, 2], [2, 3, 4], [4, 5]]
new_numbers = [num for in_list in numbers for num in in_list]
assert new_numbers == [1, 2, 2, 3, 4, 4, 5]
