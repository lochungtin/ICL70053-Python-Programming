def blankify(string):
    target = string[0]
    to_list = ["_" if char == target else char for char in list(string)]
    return "".join(to_list)


print(blankify("easy peasy lemon squeezy"))
