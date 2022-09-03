def find_in_list(numbers, query):
    try:
        position = numbers.index(query)
        return numbers[position] + numbers[position + 1]
    except ValueError:
        print("The query {} was not found in numbers. Returning 0".format(query))
        return 0
    except IndexError:
        return numbers[position]


def test_valid():
    numbers = [1, 2, 3, 4]
    result = find_in_list(numbers, 2)
    print(result)


def test_notinlist():
    numbers = [1, 2, 3, 4]
    result = find_in_list(numbers, 7)
    print(result)


def test_endoflist():
    numbers = [1, 2, 3, 4]
    result = find_in_list(numbers, 4)
    print(result)


if __name__ == "__main__":
    test_valid()
    test_notinlist()
    test_endoflist()
