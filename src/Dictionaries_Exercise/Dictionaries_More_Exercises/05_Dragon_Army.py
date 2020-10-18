class Dragon:
    def __init__(self, name, damage, health, armor):
        self.name = name
        self.damage = damage
        self.health = health
        self.armor = armor

    def __repr__(self):
        return "name:%s damage:%s health:%s armor:%s" % (self.name, self.damage, self.health, self.armor)


n = int(input())

types = {}

for _ in range(n):
    data = input().split()
    typo = data[0]
    name = data[1]
    if data[2] == "null":
        damage = 45
    else:
        damage = int(data[2])
    if data[3] == "null":
        health = 250
    else:
        health = int(data[3])
    if data[4] == "null":
        armor = 10
    else:
        armor = int(data[4])

    dragon = Dragon(name, damage, health, armor)

    if typo not in types:
        types[typo] = [dragon]
    else:
        is_found = False
        index = 0
        for elem in types[typo]:
            if elem.name == name:
                is_found = True
                index = types[typo].index(elem)
        if is_found:
            types[typo][index] = dragon
        else:
            types[typo].append(dragon)


def find_avgs(lst):
    damage_list = [obj.damage for obj in lst]
    health_list = [obj.health for obj in lst]
    armor_list = [obj.armor for obj in lst]
    avg_damage = sum(damage_list) / len(damage_list)
    avg_health = sum(health_list) / len(health_list)
    avg_armor = sum(armor_list) / len(armor_list)
    return avg_damage, avg_health, avg_armor


for typ, drags in types.items():
    print(f"{typ}::({find_avgs(drags)[0]:.2f}/{find_avgs(drags)[1]:.2f}/{find_avgs(drags)[2]:.2f})")
    sorted_drags = sorted(drags, key=lambda x: x.name)
    for drag in sorted_drags:
        print(f"-{drag.name} -> damage: {drag.damage}, health: {drag.health}, armor: {drag.armor}")
