import re


emoji_pattern = r'(?P<symbols>[:]{2}|[*]{2})(?P<name>[A-Z][a-z]{2,})\1'

text = input()

cool_threshold = 1

for s in text:
    if s.isdigit():
        cool_threshold *= int(s)

emojis = re.findall(emoji_pattern, text)
emojis_count = len(emojis)

cool_emojis = []
for item in emojis:
    coolness = 0
    for e in item[1]:
        coolness += ord(e)
    if coolness >= cool_threshold:
        cool_emojis.append(item[0]+item[1]+item[0])

print(f"Cool threshold: {cool_threshold}")
print(f"{emojis_count} emojis found in the text. The cool ones are:")
for emoji in cool_emojis:
    print(f"{emoji}")
