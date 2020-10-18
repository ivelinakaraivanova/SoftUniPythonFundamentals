import re

pattern = r"(www).([a-zA-Z0-9-]+)(\.[a-z]+)+"


while True:
    text = input()
    if text:
        matches = re.finditer(pattern, text, re.MULTILINE)

        for match in matches:
            print(match.group())
    else:
        break
