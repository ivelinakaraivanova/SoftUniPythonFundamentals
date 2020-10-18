is_obtained = False
legendary = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk_materials = {}

while not is_obtained:
    input_line = input()
    split_input = input_line.split()
    for i in range(0, len(split_input), 2):
        material = split_input[i+1].lower()
        quantity = int(split_input[i])

        if material == "shards" or material == "fragments" or material == "motes":
            key_materials[material] += quantity

            if key_materials[material] >= 250:
                key_materials[material] -= 250
                print(f"{legendary[material]} obtained!")
                is_obtained = True
                break

        else:
            if material in junk_materials:
                junk_materials[material] += quantity
            else:
                junk_materials[material] = quantity


sorted_key = sorted(key_materials.items(), key=lambda x: (-x[1], x[0]))
sorted_junk = sorted(junk_materials.items(), key=lambda x: x[0])

for material, quantity in sorted_key:
    print(f"{material}: {quantity}")

for material, quantity in sorted_junk:
    print(f"{material}: {quantity}")