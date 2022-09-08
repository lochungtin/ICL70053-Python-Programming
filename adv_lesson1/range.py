import re

pattern = "[a-z][aeiou][^0-9]"
text = ["boy", "hi!", "caT", "HEY", "art", "co2"]

for word in text:
    print(word, re.match(pattern, word))
