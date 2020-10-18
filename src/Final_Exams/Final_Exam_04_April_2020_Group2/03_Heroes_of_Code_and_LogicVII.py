def cast_spell(hero_name, mp_needed):
    if heroes[hero_name][1] >= mp_needed:
        heroes[hero_name][1] -= mp_needed
        return 1
    else:
        return -1


def take_damage(hero_name, damage):
    heroes[hero_name][0] -= damage
    if heroes[hero_name][0] > 0:
        return 1
    else:
        heroes.pop(hero_name)
        return -1


def recharge(hero_name, amount):
    if heroes[hero_name][1] + amount > max_mp:
        recharge_amount = max_mp - heroes[hero_name][1]
    else:
        recharge_amount = amount
    heroes[hero_name][1] += recharge_amount
    return recharge_amount


def heal(hero_name, amount):
    if heroes[hero_name][0] + amount > max_hp:
        heal_amount = max_hp - heroes[hero_name][0]
    else:
        heal_amount = amount
    heroes[hero_name][0] += heal_amount
    return heal_amount


n = int(input())

heroes = {}

for _ in range(n):
    data = input()
    split_data = data.split()
    hero = split_data[0]
    hp = int(split_data[1])
    mp = int(split_data[2])
    heroes[hero] = [hp, mp]

max_hp = 100
max_mp = 200

while True:
    data = input()
    if data == "End":
        break
    split_data = data.split(" - ")
    command = split_data[0]

    if command == "CastSpell":
        hero = split_data[1]
        mp_needed = int(split_data[2])
        spell_name = split_data[3]
        result = cast_spell(hero, mp_needed)
        if result == 1:
            print(f"{hero} has successfully cast {spell_name} and now has {heroes[hero][1]} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell_name}!")

    elif command == "TakeDamage":
        hero = split_data[1]
        damage = int(split_data[2])
        attacker = split_data[3]
        result = take_damage(hero, damage)
        if result == 1:
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {heroes[hero][0]} HP left!")
        else:
            print(f"{hero} has been killed by {attacker}!")

    elif command == "Recharge":
        hero = split_data[1]
        amount = int(split_data[2])
        result = recharge(hero, amount)
        print(f"{hero} recharged for {result} MP!")

    elif command == "Heal":
        hero = split_data[1]
        amount = int(split_data[2])
        result = heal(hero, amount)
        print(f"{hero} healed for {result} HP!")

sorted_heroes = dict(sorted(heroes.items(), key=lambda x: (-x[1][0], x[0])))

for key, value in sorted_heroes.items():
    print(f"{key}")
    print(f"  HP: {value[0]}")
    print(f"  MP: {value[1]}")
