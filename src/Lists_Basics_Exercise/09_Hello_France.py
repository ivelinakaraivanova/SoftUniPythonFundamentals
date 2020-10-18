items_collection = input().split("|")
budget = float(input())

bought_items = []
old_prices = 0
new_prices = 0

for item in items_collection:
    split_item = item.split("->")
    item_type = split_item[0]
    price = float(split_item[1])
    if budget >= price:
        if (item_type == "Clothes" and 0 < price <= 50) or \
                (item_type == "Shoes" and 0 <= price <= 35) or \
                (item_type == "Accessories" and 0 <= price <= 20.5):
            budget -= price
            old_prices += price
            new_prices += price * 1.4
            bought_items.append(price * 1.4)

profit = new_prices - old_prices
new_budget = budget + new_prices

for i in bought_items:
    print(f"{i:.2f} ", end="")
print()
print(f"Profit: {profit:.2f}")
if new_budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")
