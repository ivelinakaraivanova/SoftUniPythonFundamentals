product = input()
quantity = int(input())

coffee_price = 1.5
water_price = 1.00
coke_price = 1.4
snacks_price = 2.0


def order_price(prod, number):
    total_price = None
    if prod == "coffee":
        total_price = coffee_price * number
    elif prod == "water":
        total_price = water_price * number
    elif prod == "coke":
        total_price = coke_price * number
    elif prod == "snacks":
        total_price = snacks_price * number
    return f"{total_price:.2f}"


print(order_price(product, quantity))