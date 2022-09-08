import re

pattern = r"([a-z]+) \1"
text = ["die die", "d a"]

for word in text:
    print(word, re.match(pattern, word))
