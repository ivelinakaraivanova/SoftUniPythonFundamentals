'''products = {}

while True:
    input_line = input()
    if input_line == "buy":
        break
    else:
        split_input = input_line.split()
        product = split_input[0]
        price = float(split_input[1])
        quantity = int(split_input[2])
        if product in products:
            products[product][1] += quantity
            if products[product][0] != price:
                products[product][0] = price
        else:
            products[product] = [price]
            products[product].append(quantity)

for product, info in products.items():
    print(f"{product} -> {info[0]*info[1]:.2f}")
'''


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


products = []


def find_product(name:str):
    for p in products:
        if p.name == name:
            return p


while True:
    input_line = input()
    if input_line == "buy":
        break
    else:
        split_input = input_line.split()
        name = split_input[0]
        price = float(split_input[1])
        quantity = int(split_input[2])
        product = find_product(name)
        if not product:
            product = Product(name, price, quantity)
            products.append(product)
        else:
            if product.price != price:
                product.price = price
            product.quantity += quantity

for p in products:
    print(f"{p.name} -> {p.price*p.quantity:.2f}")
