import re

pattern = "(oh)( oh)*( yeah)*( baby)?"
text = [
    "oh",
    "oh oh",
    "oh oh yeah yeah yeah",
    "oh yeah yeah baby",
    "oh baby",
    "oh oh baby",
]

for word in text:
    print(word, re.match(pattern, word))
