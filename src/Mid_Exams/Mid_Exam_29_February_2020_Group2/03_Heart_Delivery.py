def jump(index):
    if neighborhood[index] >= 2:
        neighborhood[index] -= 2
        if neighborhood[index] == 0:
            print(f"Place {index} has Valentine's day.")
    else:
        print(f"Place {index} already had Valentine's day.")


neighborhood = list(map(int, input().split("@")))
current_index = 0

while True:
    command = input()
    if command == "Love!":
        break
    else:
        length = int(command.split()[1])
        current_index += length

        if current_index in range(len(neighborhood)):
            jump(current_index)
        else:
            current_index = 0
            jump(current_index)

print(f"Cupid's last position was {current_index}.")

count_fails = 0
for item in neighborhood:
    if item != 0:
        count_fails += 1
if count_fails == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {count_fails} places.")


