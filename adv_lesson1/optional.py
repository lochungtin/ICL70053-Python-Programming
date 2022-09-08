import re

pattern = "[0-9]+ files? found"
text = ["0 file found", "1 file found", "13 files found"]

for word in text:
    print(word, re.match(pattern, word))
