users = {}

n = int(input())

for _ in range(n):
    command = input().split()
    service = command[0]
    username = command[1]

    if service == "register":
        license_number = command[2]
        if username not in users:
            users[username] = license_number
            print(f"{username} registered {license_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_number}")

    elif service == "unregister":
        if username not in users:
            print(f"ERROR: user {username} not found")
        else:
            users.pop(username)
            print(f"{username} unregistered successfully")

for user, license_num in users.items():
    print(f"{user} => {license_num}")