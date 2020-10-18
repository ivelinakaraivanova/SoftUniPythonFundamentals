import re

text = input().lower()
word = input().lower()

pattern = '\\b' + word + '\\b'

split_text = re.findall(pattern, text)

count = len(split_text)
print(count)
