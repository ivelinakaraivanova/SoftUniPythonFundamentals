def like(guest_name, meal_name):
    if guest_name not in guests:
        guests[guest_name] = [meal_name]
    else:
        if meal_name not in guests[guest_name]:
            guests[guest_name].append(meal_name)


def unlike(guest_name, meal_name):
    if guest_name not in guests:
        return -1
    else:
        if meal_name not in guests[guest_name]:
            return -2
        else:
            guests[guest_name].remove(meal_name)
            return 1


guests = {}
unlike_count = 0

while True:
        data = input()
        if data == "Stop":
            break
        split_data = data.split("-")
        command = split_data[0]

        if command == "Like":
            guest = split_data[1]
            meal = split_data[2]
            like(guest, meal)

        elif command == "Unlike":
            guest = split_data[1]
            meal = split_data[2]
            result = unlike(guest, meal)
            if result == -1:
                print(f"{guest} is not at the party.")
            elif result == -2:
                print(f"{guest} doesn't have the {meal} in his/her collection.")
            elif result == 1:
                unlike_count += 1
                print(f"{guest} doesn't like the {meal}.")

sorted_guests = dict(sorted(guests.items(), key=lambda x: (-len(x[1]), x[0])))

for key, value in sorted_guests.items():
    print(f"{key}: " + ", ".join(value))

print(f"Unliked meals: {unlike_count}")
