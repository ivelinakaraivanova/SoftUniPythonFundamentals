stock = input().split()
searched_products = input().split()

bakery = {}

for element in range(0, len(stock), 2):
    product = stock[element]
    quantity = stock[element+1]
    bakery[product] = int(quantity)

for item in searched_products:
    if item in bakery:
        print(f"We have {bakery[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")

