dwarfs = {}

while True:
    data = input()
    if data == "Once upon a time":
        break
    else:
        split_data = data.split(" <:> ")
        name = split_data[0]
        hat_color = split_data[1]
        physics = int(split_data[2])

        if hat_color not in dwarfs:
            dwarfs[hat_color] = {name: physics}
        else:
            if name not in dwarfs[hat_color]:
                dwarfs[hat_color][name] = physics
            else:
                if dwarfs[hat_color][name] < physics:
                    dwarfs[hat_color][name] = physics

sorted_dwarf = sorted(dwarfs.items(), key=lambda x: -len(x[1]))

new_dict = {}
for element in sorted_dwarf:
    for k, v in element[1].items():
        new_dict[element[0]+":"+k] = v
        
sorted_new = sorted(new_dict.items(), key=lambda x: -x[1])

for tup in sorted_new:
    hat_color = tup[0].split(':')[0]
    name = tup[0].split(':')[1]
    physics = tup[1]
    print(f"({hat_color}) {name} <-> {physics}")