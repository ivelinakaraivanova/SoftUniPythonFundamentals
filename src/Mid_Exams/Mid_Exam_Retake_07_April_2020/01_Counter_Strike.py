energy = int(input())

won_battles = 0

while True:
    input_line = input()
    if input_line == "End of battle":
        print(f"Won battles: {won_battles}. Energy left: {energy}")
        break
    else:
        distance = int(input_line)
        if energy >= distance:
            energy -= distance
            won_battles += 1
            if won_battles % 3 == 0:
                energy += won_battles
        else:
            print(f"Not enough energy! Game ends with {won_battles} won battles and {energy} energy")
            break
