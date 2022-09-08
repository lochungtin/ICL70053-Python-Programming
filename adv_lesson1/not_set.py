import re

pattern = "[^aeiou].."
text = ["hey", "cod", "boy", "you", "ant", "ear"]

for word in text:
    print(word, re.match(pattern, word))
