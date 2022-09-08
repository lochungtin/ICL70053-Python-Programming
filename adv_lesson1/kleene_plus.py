import re

pattern = "[xyz]+"
text = ["x", "y", "z", " "]

for word in text:
    print(word, re.match(pattern, word))
