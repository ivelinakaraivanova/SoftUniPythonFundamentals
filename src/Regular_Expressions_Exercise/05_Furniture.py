import re

pattern = r">>([A-Za-z]+)<<((\d+)(\.\d+)?)!(\d+)"

furnitures = []
total_price = 0

while True:
    text = input()
    if text == "Purchase":
        break
    else:
        matches = re.findall(pattern, text)

        for match in matches:
            furniture = match[0]
            quantity = int(match[4])
            price = float(match[1])
            total_price += price * quantity
            furnitures.append(furniture)

print("Bought furniture:")
for f in furnitures:
    print(f"{f}")
print(f"Total money spend: {total_price:.2f}")
