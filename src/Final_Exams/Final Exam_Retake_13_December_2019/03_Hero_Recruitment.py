def enroll(hero):
    if hero not in heroes:
        heroes[hero] = []
        return 1
    else:
        return -1


def learn(hero, spell):
    if hero not in heroes:
        return -1
    else:
        if spell in heroes[hero]:
            return -2
        else:
            heroes[hero].append(spell)


def unlearn(hero, spell):
    if hero not in heroes:
        return -1
    else:
        if spell not in heroes[hero]:
            return -2
        else:
            heroes[hero].remove(spell)


heroes = {}

while True:
    input_command = input()
    if input_command == "End":
        break
    else:
        split_command = input_command.split()
        command = split_command[0]

        if command == "Enroll":
            hero_name = split_command[1]
            result = enroll(hero_name)
            if result == -1:
                print(f"{hero_name} is already enrolled.")

        elif command == "Learn":
            hero_name = split_command[1]
            spell_name = split_command[2]
            result = learn(hero_name, spell_name)
            if result == -1:
                print(f"{hero_name} doesn't exist.")
            elif result == -2:
                print(f"{hero_name} has already learnt {spell_name}.")

        elif command == "Unlearn":
            hero_name = split_command[1]
            spell_name = split_command[2]
            result = unlearn(hero_name, spell_name)
            if result == -1:
                print(f"{hero_name} doesn't exist.")
            elif result == -2:
                print(f"{hero_name} doesn't know {spell_name}.")

sorted_heroes = dict(sorted(heroes.items(), key=lambda x: (-len(x[1]), x[0])))

print("Heroes:")

for key, value in sorted_heroes.items():
    print(f"== {key}: " + ", ".join(value))
