import re

pattern = "b.*!"
text = ["b!, ba!, bdsf^123!", "daaad!, ba1a?2@cd"]

for word in text:
    print(word, re.match(pattern, word))
