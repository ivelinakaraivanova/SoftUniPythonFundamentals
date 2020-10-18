force = {}

while True:
    input_line = input()
    if input_line == "Lumpawaroo":
        break
    else:
        if "|" in input_line:
            split_input = input_line.split(" | ")
            force_side = split_input[0]
            force_user = split_input[1]
            is_found = False
            for key, value in force.items():
                if force_user in value:
                    is_found = True
            if not is_found:
                if force_side not in force:
                    force[force_side] = [force_user]
                else:
                    if force_user not in force[force_side]:
                        force[force_side].append(force_user)

        elif "->" in input_line:
            split_input = input_line.split(" -> ")
            force_side = split_input[1]
            force_user = split_input[0]

            for key, value in force.items():
                if force_user in value:
                    force[key].pop(value.index(force_user))

            if force_side not in force:
                force[force_side] = [force_user]
            else:
                force[force_side].append(force_user)

            print(f"{force_user} joins the {force_side} side!")

sorted_force = sorted(force.items(), key=lambda x: (-len(x[1]), x[0]))

for side in sorted_force:
    if len(side[1]) > 0:
        print(f"Side: {side[0]}, Members: {len(side[1])}")
        for u in sorted(side[1]):
            print(f"! {u}")