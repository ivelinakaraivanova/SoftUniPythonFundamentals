def add_animal(name, limit, area):
    if name not in animal_list:
        animal_list.append(name)
        food_list.append(int(limit))
        area_list.append(area)
    elif area in area_list:
        index = animal_list.index(name)
        food_list[index] += int(limit)


def feed_animal(name, food, area):
    if name in animal_list and area in area_list:
        index = animal_list.index(name)
        food_list[index] -= int(food)
        if food_list[index] <= 0:
            animal_list.pop(index)
            area_list.pop(index)
            food_list.pop(index)
            print(f"{name} was successfully fed")


animal_list = []
food_list = []
area_list = []

is_last_info = False

while not is_last_info:
    command = input()
    if command == "Last Info":
        is_last_info = True
    else:
        token = command.split(":")
        action = token[0]
        animal_name = token[1]
        food_limit = token[2]
        area_name = token[3]
        if action == "Add":
            add_animal(animal_name, food_limit, area_name)
        elif action == "Feed":
            feed_animal(animal_name, food_limit, area_name)

animals_foods_list = list(map(lambda x, y: [x, y], animal_list, food_list))
animals_foods_sorted = sorted(animals_foods_list, key=lambda x: [-x[1], x[0]])

print("Animals:")
for animal in animals_foods_sorted:
    print(f"{animal[0]} -> {animal[1]}g")

area_count_list = [(area, area_list.count(area)) for area in area_list]
area_set = list(set(area_count_list))
area_list_sorted = sorted(area_set, key=lambda x: -x[1])

print("Areas with hungry animals:")
for area in area_list_sorted:
    print(f"{area[0]} : {area[1]}")

