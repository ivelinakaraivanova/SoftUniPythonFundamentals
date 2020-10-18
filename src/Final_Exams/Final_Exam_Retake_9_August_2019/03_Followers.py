


followers = {}

while True:
    data = input()
    if data == "Log out":
        break
    split_data = data.split(": ")
    command = split_data[0]

    if command == "New follower":
        username = split_data[1]
        if username not in followers:
            followers[username] = [0, 0]

    elif command == "Like":
        username = split_data[1]
        count = int(split_data[2])
        if username not in followers:
            followers[username] = [0, 0]
            followers[username][1] = count
        else:
            followers[username][1] += count

    elif command == "Comment":
        username = split_data[1]
        if username not in followers:
            followers[username] = [0, 0]
            followers[username][0] = 1
        else:
            followers[username][0] += 1

    elif command == "Blocked":
        username = split_data[1]
        if username in followers:
            followers.pop(username, None)
        else:
            print(f"{username} doesn't exist.")

sorted_followers = dict(sorted(followers.items(), key=lambda x: (-x[1][1], x[0])))

print(f"{len(followers)} followers")
for key, value in sorted_followers.items():
    likes = value[0]
    comments = value[1]
    print(f"{key}: {likes+comments}")
