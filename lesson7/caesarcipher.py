def apply_shift(ch, shift):
    base = 65
    if ch.islower():
        base = 97

    return chr(base + (26 + ord(ch) - base + shift) % 26)


def apply_cipher(string, shift=0):
    return "".join(
        [apply_shift(char, shift) if char.isalpha() else char for char in list(string)]
    )


print(apply_cipher("THE quick Brown fox JuMpS Over the lazy dog", -3))
