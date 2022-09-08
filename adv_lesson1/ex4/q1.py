import re

pattern = "^[a-zA-Z0-9_.?+-]+@[a-zA-Z0-9-]*[a-zA-Z][a-zA-Z0-9]*\.(com?|org)$"
text = ["123@-gmail.com", "123@gmail.com", "1234"]

for word in text:
    print(word, re.search(pattern, word))
