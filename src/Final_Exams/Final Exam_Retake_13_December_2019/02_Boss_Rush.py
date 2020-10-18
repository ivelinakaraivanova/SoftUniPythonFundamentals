import re

pattern = r'\|(?P<name>[A-Z]{4,})\|:#(?P<title>[a-zA-Z]+\s[a-zA-Z]+)#'

n = int(input())

for _ in range(n):
    text = input()
    if re.search(pattern, text) is not None:
        matches = re.finditer(pattern, text)
        for match in matches:
            boss_name = match.group('name')
            title = match.group('title')
            length_boss_name = len(boss_name)
            length_title = len(title)
            print(f"{boss_name}, The {title}")
            print(f">> Strength: {length_boss_name}")
            print(f">> Armour: {length_title}")
    else:
        print("Access denied!")
