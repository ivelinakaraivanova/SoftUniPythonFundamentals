users = {}
languages = {}

while True:
    data = input()
    if data == "exam finished":
        break
    else:
        split_data = data.split("-")
        username = split_data[0]
        if len(split_data) > 2:
            language = split_data[1]
            points = int(split_data[2])

            if username not in users:
                users[username] = [points]
            else:
                users[username].append(points)

            if language not in languages:
                languages[language] = 1
            else:
                languages[language] += 1

        else:
            users.pop(username)

sorted_users = sorted(users.items(), key=lambda x: (-max(x[1]), x[0]))
sorted_languages = sorted(languages.items(), key=lambda x: (-x[1], x[0]))

print("Results:")
for user in sorted_users:
    print(f"{user[0]} | {max(user[1])}")

print("Submissions:")
for lang in sorted_languages:
    print(f"{lang[0]} - {lang[1]}")