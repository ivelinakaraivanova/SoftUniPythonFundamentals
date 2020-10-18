budget = float(input())
flour_price = float(input())

eggs_price = flour_price * 0.75
milk_price = (flour_price * 1.25) * 0.25
cozonac_price = flour_price + eggs_price + milk_price

colored_eggs = 0
cozonac_count = 0

while cozonac_price < budget:
    budget -= cozonac_price
    cozonac_count += 1
    colored_eggs += 3
    if cozonac_count % 3 == 0:
        colored_eggs -= cozonac_count - 2

print(f"You made {cozonac_count} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")


