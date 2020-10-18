events_list = input().split("|")

initial_energy = 100
initial_coins = 100

current_energy = initial_energy
coins = initial_coins
not_all_actions = False

for event in events_list:
    split_event = event.split("-")
    name = split_event[0]
    number = int(split_event[1])

    if name == "rest":
        gained_energy = 0
        if number + current_energy < 100:
            gained_energy = number
            current_energy += number
        else:
            gained_energy = 100 - current_energy
            current_energy = 100
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {current_energy}.")

    elif name == "order":
        if current_energy < 30:
            current_energy += 50
            print("You had to rest!")

            continue

        coins += number
        current_energy -= 30
        print(f"You earned {number} coins.")

    else:
        if coins - number <= 0:
            print(f"Closed! Cannot afford {name}.")
            not_all_actions = True
            break

        coins -= number
        print(f"You bought {name}.")

if not not_all_actions:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {current_energy}")