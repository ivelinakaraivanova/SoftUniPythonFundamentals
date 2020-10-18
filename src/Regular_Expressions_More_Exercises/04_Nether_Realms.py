import re

split_pattern = r'[\s,]+'
chars_pattern = r'[A-Za-z]*[^0-9\.\+\-\*\/\s]+'
number_pattern = r'[+-]?[\d+\.]*[\d]+'
sign_pattern = r'[*\|/]'

text = input()
split_text = re.split(split_pattern, text)

demons = {}

for demon in split_text:
    health = 0
    string = ''

    char_matches = re.findall(chars_pattern, demon)
    for match in char_matches:
        string += match
    for char in string:
        health += ord(char)

    number_matches = re.findall(number_pattern, demon)

    damage = 0
    for num in number_matches:
        damage += float(num)

    sign_matches = re.findall(sign_pattern, demon)
    for sign in sign_matches:
        if sign == '*':
            damage *= 2
        elif sign == '/':
            damage /= 2

    demons[demon] = [health, damage]

sorted_demons = dict(sorted(demons.items(), key=lambda x: x[0]))

for demon, info in sorted_demons.items():
    print(f"{demon} - {info[0]} health, {info[1]:.2f} damage")
