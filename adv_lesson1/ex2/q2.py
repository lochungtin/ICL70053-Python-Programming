import re

pattern = "^[a-z]*b$"
text = ["bob", "Bob", "britney"]

for word in text:
    print(word, re.search(pattern, word))
