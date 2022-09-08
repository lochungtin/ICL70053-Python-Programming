import re

pattern = "^b?(b+ab+)*b?$"
text = ["bab", "babbab", "bb", "", "a", "abba"]

for word in text:
    print(word, re.search(pattern, word))
