contests = {}
users = {}

while True:
    data = input()
    if data == "end of contests":
        break
    else:
        contest, password = data.split(":")
        if contest not in contests:
            contests[contest] = password

while True:
    data = input()
    if data == "end of submissions":
        break
    else:
        contest = data.split("=>")[0]
        password = data.split("=>")[1]
        username = data.split("=>")[2]
        points = int(data.split("=>")[3])
        if contest in contests:
            if password == contests[contest]:
                if username not in users:
                    users[username] = [[contest, points]]
                else:
                    is_found = False
                    index = None
                    for element in users[username]:
                        if element[0] == contest:
                            is_found = True
                            index = users[username].index(element)
                    if is_found:
                        if users[username][index][1] < points:
                            users[username][index][1] = points
                    else:
                        users[username].append([contest, points])

max_points = 0
max_user = ''

for user, info in users.items():
    total_points = 0
    for element in info:
        total_points += element[1]
    if total_points > max_points:
        max_points = total_points
        max_user = user

print(f"Best candidate is {max_user} with total {max_points} points.")

sorted_users = sorted(users.items(), key=lambda x: x[0])

print("Ranking:")
for user in sorted_users:
    print(f"{user[0]}")
    for el in sorted(user[1], key=lambda x: -x[1]):
        print(f"#  {el[0]} -> {el[1]}")
