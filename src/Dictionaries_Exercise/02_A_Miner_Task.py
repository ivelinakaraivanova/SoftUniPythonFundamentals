strings = {}

while True:
    resource = input()

    if resource == "stop":
        break
    else:
        quantity = int(input())
        if resource in strings:
            strings[resource] += quantity
        else:
            strings[resource] = quantity

for resource, quantity in strings.items():
    print(f"{resource} -> {quantity}")