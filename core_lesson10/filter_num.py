def is_palindrome(num):
    string = str(num)
    length = len(string)
    half_length = length // 2

    for i in range(half_length):
        if string[i] != string[length - i - 1]:
            return False

    return True


numbers = range(100, 300)
palindromes = list(filter(is_palindrome, numbers))
assert palindromes == [
    101,
    111,
    121,
    131,
    141,
    151,
    161,
    171,
    181,
    191,
    202,
    212,
    222,
    232,
    242,
    252,
    262,
    272,
    282,
    292,
]
