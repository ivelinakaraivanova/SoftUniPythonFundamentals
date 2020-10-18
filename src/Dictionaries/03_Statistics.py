products = {}

while True:
    input_line = input()
    if input_line == "statistics":
        break
    else:
        product = input_line.split(": ")[0]
        quantity = int(input_line.split(": ")[1])
        if product in products:
            products[product] += quantity
        else:
            products[product] = quantity

products_count = 0
quantities_count = 0

print("Products in stock:")
for product, quantity in products.items():
    print(f"- {product}: {quantity}")
    products_count += 1
    quantities_count += quantity
print(f"Total Products: {products_count}")
print(f"Total Quantity: {quantities_count}")

# print(f"Total Products: {len(products.keys())}")
# print(f"Total Quantity: {sum(products.values())}")
