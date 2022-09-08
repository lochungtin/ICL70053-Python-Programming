import re

pattern = "[0-9]{3,7}"
text = ["123", "1234678", "12", "12347809"]

for word in text:
    print(word, re.match(pattern, word))
