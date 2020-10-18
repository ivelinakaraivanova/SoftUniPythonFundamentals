def add(name, health, energy):
    if name not in people:
        people[name] = [health, energy]
    else:
        people[name][0] += health


def attack(attacker_name, defender_name, damage):
    result = 0
    if attacker_name in people and defender_name in people:
        people[defender_name][0] -= damage
        if people[defender_name][0] <= 0:
            people.pop(defender_name)
            result -= 1
        people[attacker_name][1] -= 1
        if people[attacker_name][1] <= 0:
            people.pop(attacker_name)
            result -= 2
    return result


def delete(name):
    if name == "All":
        people.clear()
    elif name in people:
        people.pop(name)


people = {}

while True:
    data = input()
    if data == "Results":
        break
    split_data = data.split(":")
    command = split_data[0]

    if command == "Add":
        person_name = split_data[1]
        health = int(split_data[2])
        energy = int(split_data[3])
        add(person_name, health, energy)

    elif command == "Attack":
        attacker_name = split_data[1]
        defender_name = split_data[2]
        damage = int(split_data[3])
        result = attack(attacker_name, defender_name, damage)
        if result == -1 or result == -3:
            print(f"{defender_name} was disqualified!")
        if result == -2 or result == -3:
            print(f"{attacker_name} was disqualified!")

    elif command == "Delete":
        person_name = split_data[1]
        delete(person_name)

sorted_people = dict(sorted(people.items(), key=lambda x: (-x[1][0], x[0])))

print(f"People count: {len(people)}")
for key, value in sorted_people.items():
    print(f"{key} - {value[0]} - {value[1]}")