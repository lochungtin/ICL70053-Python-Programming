import re

pattern = "gr(a|e)y"
text = ["grey", "gray"]

for word in text:
    print(word, re.match(pattern, word))
