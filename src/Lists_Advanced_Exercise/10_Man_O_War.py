def is_valid_index(data_list, index_number):
    return (0 <= index_number) and (index_number < len(data_list))


def is_sank(data_list, ind):
    if is_valid_index(data_list, ind):
        return data_list[ind] <= 0


def fire(data_list, index_number, damage_number):
    if is_valid_index(data_list, index_number):
        data_list[index_number] -= damage_number


def defend(data_list, start_index_number, end_index_number, damage_number):
    if is_valid_index(data_list, start_index_number) and is_valid_index(data_list, end_index_number):
        for ind in range(start_index_number, end_index_number+1):
            data_list[ind] -= damage_number


def repair(data_list, index_number, health_number):
    if is_valid_index(data_list, index_number):
        data_list[index_number] += health_number
        if data_list[index_number] > maximum:
            data_list[index_number] = maximum


def status(data_list):
    low = [c for c in data_list if c < maximum*0.2]
    return len(low)


pirate_ship = list(map(int, input().split(">")))
warship = list(map(int, input().split(">")))
maximum = int(input())
is_retire = False
is_stalemate = True

while not is_retire:
    command = input()
    if command == "Retire":
        is_retire = True
    else:
        token = command.split()
        action = token[0]

        if action == "Fire":
            index = int(token[1])
            damage = int(token[2])
            fire(warship, index, damage)
            if is_sank(warship, index):
                print("You won! The enemy ship has sunken.")
                is_stalemate = False
                break

        elif action == "Defend":
            start_index = int(token[1])
            end_index = int(token[2])
            damage = int(token[3])
            defend(pirate_ship, start_index, end_index, damage)
            for i in range(len(pirate_ship)):
                if is_sank(pirate_ship, i):
                    print("You lost! The pirate ship has sunken.")
                    is_stalemate = False
                    break

        elif action == "Repair":
            index = int(token[1])
            health = int(token[2])
            repair(pirate_ship, index, health)

        elif action == "Status":
            count = status(pirate_ship)
            print(f"{count} sections need repair.")

if is_stalemate:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(warship)}")
