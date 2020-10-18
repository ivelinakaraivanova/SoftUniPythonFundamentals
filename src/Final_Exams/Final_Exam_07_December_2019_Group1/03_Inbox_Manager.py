users = {}

while True:
    data = input()
    if data == "Statistics":
        break
    split_data = data.split("->")
    command = split_data[0]

    if command == "Add":
        user = split_data[1]
        if user in users:
            print(f"{user} is already registered")
        else:
            users[user] = []

    elif command == "Send":
        user = split_data[1]
        email = split_data[2]
        users[user].append(email)

    elif command == "Delete":
        user = split_data[1]
        if user in users:
            users.pop(user, None)
        else:
            print(f"{user} not found!")

sorted_users = dict(sorted(users.items(), key=lambda x: (-len(x[1]), x[0])))

print(f"Users count: {len(users)}")
for key, value in sorted_users.items():
    print(f"{key}")
    for email in value:
        print(f" - {email}")
        