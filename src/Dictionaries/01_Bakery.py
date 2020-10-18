input_line = input().split()

bakery = {}

for element in range(0, len(input_line), 2):
    key = input_line[element]
    value = input_line[element+1]
    bakery[key] = int(value)

print(bakery)

# dictionary comprehension
# bakery = {input_line[element]: int(input_line[element+1]) for element in range(0, len(input_line), 2)}
