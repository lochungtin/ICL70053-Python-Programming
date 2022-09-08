import re

pattern = "^(a.)*a?$"
text = ["a", "ac", "aba", "ababa", "baba"]

for word in text:
    print(word, re.search(pattern, word))
