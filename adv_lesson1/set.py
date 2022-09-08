import re

pattern = "[a-z]an"
text = ["can", "fan", "man", "men"]

for word in text:
    print(word, re.match(pattern, word))
