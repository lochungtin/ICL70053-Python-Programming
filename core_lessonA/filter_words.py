words = ["Oh", "I", "wanna", "dance", "with", "somebody"]
long_words = list(filter(lambda x: len(x) > 4, words))
assert long_words == ["wanna", "dance", "somebody"]
