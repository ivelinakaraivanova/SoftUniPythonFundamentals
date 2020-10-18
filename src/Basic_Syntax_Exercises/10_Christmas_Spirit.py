quantity = int(input())
days = int(input())

ornament_set = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15

total_costs = 0
total_spirit = 0

for day in range(1, days+1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        total_costs += ornament_set * quantity
        total_spirit += 5
    if day % 3 == 0:
        total_costs += (tree_skirt + tree_garland) * quantity
        total_spirit += 13
    if day % 5 == 0:
        total_costs += tree_lights * quantity
        total_spirit += 17
    if day % 10 == 0:
        total_costs += tree_skirt + tree_garland + tree_lights
        total_spirit -= 20
    if day % 15 == 0:
        total_spirit += 30
if days % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {total_costs}")
print(f"Total spirit: {total_spirit}")