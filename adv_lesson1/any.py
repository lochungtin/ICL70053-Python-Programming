import re

pattern = ".e.e"
text = ["hehe", "eeaa"]

for word in text:
    print(word, re.match(pattern, word))
