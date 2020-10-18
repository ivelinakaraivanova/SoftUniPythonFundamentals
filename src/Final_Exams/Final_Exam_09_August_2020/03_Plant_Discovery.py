def rate(plant_name, rating_number):
    if plant_name in plants:
        plants[plant_name][1].append(rating_number)
        return 1
    else:
        return -1


def update(plant_name, new_rarity):
    if plant_name in plants:
        plants[plant_name][0] = new_rarity
        return 1
    else:
        return -1


def reset(plant_name):
    if plant_name in plants:
        plants[plant_name][1] = []
        return 1
    else:
        return -1


n = int(input())

plants = {}

for _ in range(n):
    data = input()
    split_data = data.split("<->")
    plant = split_data[0]
    rarity = int(split_data[1])

    if plant not in plants:
        plants[plant] = [rarity, []]
    else:
        plants[plant] = [rarity, []]


while True:
    input_commands = input()
    if input_commands == "Exhibition":
        break
    split_commands = input_commands.split(": ")
    command = split_commands[0]
    split_command_data = split_commands[1].split(" - ")

    if command == "Rate":
        plant = split_command_data[0]
        rating = int(split_command_data[1])
        result = rate(plant, rating)
        if result == -1:
            print("error")

    elif command == "Update":
        plant = split_command_data[0]
        new_rarity = int(split_command_data[1])
        result = update(plant, new_rarity)
        if result == -1:
            print("error")

    elif command == "Reset":
        plant = split_commands[1]
        result = reset(plant)
        if result == -1:
            print("error")

average_plants = {}
for plant, value in plants.items():
    if len(value[1]) > 0:
        avg = sum(value[1])/len(value[1])
        average_plants[plant] = [value[0], avg]
    else:
        average_plants[plant] = [value[0], len(value[1])]

sorted_plants = dict(sorted(average_plants.items(), key=lambda x: (-x[1][0], -x[1][1])))

print("Plants for the exhibition:")

for key, value in sorted_plants.items():
    print(f"- {key}; Rarity: {value[0]}; Rating: {value[1]:.2f}")

