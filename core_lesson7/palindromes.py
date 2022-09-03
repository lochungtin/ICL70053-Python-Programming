def format_string(string):
    return "".join([char.lower() if char.isalpha() else "" for char in list(string)])


def is_palindrome(string):
    string = format_string(string)

    length = len(string)
    half_length = length // 2

    for i in range(half_length):
        if string[i] != string[length - i - 1]:
            return False

    return True


print(is_palindrome("Eva, can I see bees in a cave?a"))
