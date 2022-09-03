def is_palindrome(string):
    length = len(string)
    half_length = length // 2

    for i in range(half_length):
        if string[i] != string[length - i - 1]:
            return False

    return True


print(is_palindrome("kayyak"))
