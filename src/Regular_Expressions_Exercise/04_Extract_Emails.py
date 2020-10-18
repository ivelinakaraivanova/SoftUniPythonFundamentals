import re

text = input()

pattern = r'( |^)[a-zA-Z0-9]+((\-|\.|\_)?[a-zA-Z0-9]+)*@[a-zA-Z]+(-[a-zA-Z-]+)*(\.[a-zA-Z]+(-[a-zA-Z]+)*)+'

matches = re.finditer(pattern, text)

for match in matches:
    print(match[0])

'''
user_pattern = [a-zA-Z0-9]+((\-|\.|\_)[a-zA-Z0-9]+)*
host_pattern = [a-zA-Z]+(-[a-zA-Z-]+)*(\.[a-zA-Z]+(-[a-zA-Z-]+)*)+
pattern = rf"{user_pattern}@{host_pattern}"
'''