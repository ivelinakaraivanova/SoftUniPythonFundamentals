rooms = input().split("|")
health = 100
bitcoins = 0

room_count = 0
is_broken = False

for room in rooms:
    split_room = room.split()
    command = split_room[0]
    number = int(split_room[1])
    room_count += 1

    if command == "potion":
        addition = 0

        if health + number > 100:
            addition = 100 - health
        else:
            addition = number

        health += addition
        print(f"You healed for {addition} hp.")
        print(f"Current health: {health} hp.")

    elif command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")

    else:
        health -= number
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room_count}")
            is_broken = True
            break

if not is_broken:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")