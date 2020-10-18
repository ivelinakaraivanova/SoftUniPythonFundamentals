data = input()
digits = ""
letters = ""
symbols = ""

for c in data:
    if c.isdigit():
        digits += c
    elif c.isalpha():
        letters += c
    else:
        symbols += c

print(digits)
print(letters)
print(symbols)