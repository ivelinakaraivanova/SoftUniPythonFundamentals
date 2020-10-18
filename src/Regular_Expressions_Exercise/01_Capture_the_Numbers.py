import re

input_texts_list = []

while True:
    input_text = input()
    if input_text:
        input_texts_list += [input_text]
    else:
        break


pattern = r'\d+'

for item in input_texts_list:
    matches = re.finditer(pattern, item)
    for m in matches:
        print(m.group(), end=' ')