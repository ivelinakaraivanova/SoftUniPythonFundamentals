def plunder(town, people_num, gold_amount):
    targets[town][0] -= people_num
    targets[town][1] -= gold_amount
    if (targets[town][0]) > 0 and (targets[town][1] > 0):
        return 1
    else:
        targets.pop(town)
        return -1


def prosper(town, gold_amount):
    if gold_amount >= 0:
        targets[town][1] += gold_amount
        return 1
    else:
        return -1


targets = {}

while True:
    data = input()
    if data == "Sail":
        break
    split_data = data.split("||")
    city = split_data[0]
    population = int(split_data[1])
    gold = int(split_data[2])
    if city not in targets:
        targets[city] = [population, gold]
    else:
        targets[city][0] += population
        targets[city][1] += gold

while True:
    command = input()
    if command == "End":
        break
    split_command = command.split("=>")
    action = split_command[0]

    if action == "Plunder":
        town = split_command[1]
        people = int(split_command[2])
        gold = int(split_command[3])
        result = plunder(town, people, gold)
        if result == 1:
            print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        elif result == -1:
            print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
            print(f"{town} has been wiped off the map!")

    elif action == "Prosper":
        town = split_command[1]
        gold = int(split_command[2])
        result = prosper(town, gold)
        if result == 1:
            print(f"{gold} gold added to the city treasury. {town} now has {targets[town][1]} gold.")
        else:
            print("Gold added cannot be a negative number!")

if len(targets) > 0:
    sorted_targets = dict(sorted(targets.items(), key=lambda x: (-x[1][1], x[0])))
    print(f"Ahoy, Captain! There are {len(targets)} wealthy settlements to go to:")
    for key, value in sorted_targets.items():
        print(f"{key} -> Population: {value[0]} citizens, Gold: {value[1]} kg")

else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
