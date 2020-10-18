import re

pattern = r'^\%([A-Z][a-z]*)\%[^|$%.]*\<(\w+)\>[^|$%.]*\|([0-9]+)\|[^|$%.]*?(\d+(\.\d+)?)\$$'

total_income = 0

while True:
    text = input()
    if text == "end of shift":
        break
    matches = re.finditer(pattern, text)
    for match in matches:
        customer = match[1]
        product = match[2]
        count = int(match[3])
        price = float(match[4])
        total_price = count * price
        print(f"{customer}: {product} - {total_price:.2f}")
        total_income += total_price

print(f"Total income: {total_income:.2f}")