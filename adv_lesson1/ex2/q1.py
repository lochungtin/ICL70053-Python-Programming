import re

pattern = "^([A-Za-z]|\s)*$"
text = ["Hello World", "1234"]

for word in text:
    print(word, re.search(pattern, word))
