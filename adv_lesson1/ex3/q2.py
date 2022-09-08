import re

pattern = "^([a-z]|_)([a-z0-9]|_)* = -?\d(\.\d)?$"
text = ["my_var = -2.1", "_var = 2", "1 = 1"]

for word in text:
    print(word, re.search(pattern, word))
