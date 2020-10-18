import re

pattern = r'!(?P<command>[A-Z][a-z]{2,})!:\[(?P<message>[a-zA-Z]{8,})\]'

n = int(input())

for _ in range(n):
    text = input()
    if re.search(pattern, text) is not None:
        matches = re.finditer(pattern, text)
        for match in matches:
            command = match.group('command')
            message = match.group('message')
            ascii_codes = [str(ord(s)) for s in message]
            print(f"{command}: " + ' '.join(ascii_codes))
    else:
        print("The message is invalid")

