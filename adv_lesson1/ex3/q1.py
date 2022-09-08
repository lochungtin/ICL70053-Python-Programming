import re

pattern = "^([a-z]|_)([a-z0-9]|_)*$"
text = ["my_var", "_var", "1234"]

for word in text:
    print(word, re.search(pattern, word))
