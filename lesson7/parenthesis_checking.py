def is_parenthesis_balanced(string):
    stack = []

    chars = list(string)
    for char in chars:
        if char == ")":
            if len(stack) == 0:
                return False

            stack.pop()

        elif char == "(":
            stack.append("(")

    return len(stack) == 0


print(is_parenthesis_balanced("(()())"))
