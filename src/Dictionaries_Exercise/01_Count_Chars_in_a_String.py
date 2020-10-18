string = input()

chars = {}

for ch in string:
    if ch != " ":
        if ch in chars:
            chars[ch] += 1
        else:
            chars[ch] = 1

for char, count in chars.items():
    print(f"{char} -> {count}")