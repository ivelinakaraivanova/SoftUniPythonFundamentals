import re

pattern = r'(?P<sym>[^\s]+)>(?P<numbers>[\d]{3})\|(?P<lowletters>[a-z]{3})\|(?P<upletters>[A-Z]{3})\|' \
          r'(?P<symbols>[^<>]{3})<\1'

n = int(input())

for _ in range(n):
    text = input()
    if re.search(pattern, text) is not None:
        matches = re.finditer(pattern, text)
        for match in matches:
            numbers = match.group('numbers')
            lower_letters = match.group('lowletters')
            upper_letters = match.group('upletters')
            symbols = match.group('symbols')
            print(f"Password: {numbers+lower_letters+upper_letters+symbols}")
    else:
        print("Try another password!")
