import copy


def minmax_swap(number):
    numbers = set()
    numbers.add(number)

    digits = [int(digit) for digit in str(number)]
    for i in range(len(digits) - 1):
        for j in range(i + 1, len(digits)):
            swapped_digits = copy.deepcopy(digits)
            swapped_digits[i], swapped_digits[j] = swapped_digits[j], swapped_digits[i]
            if swapped_digits[0] > 0:
                numbers.add(int("".join([str(digit) for digit in swapped_digits])))

    return min(numbers), max(numbers)
