contests = {}

while True:
    data = input()
    if data == "no more time":
        break
    else:
        user = data.split(" -> ")[0]
        contest = data.split(" -> ")[1]
        points = int(data.split(" -> ")[2])

        if contest not in contests:
            contests[contest] = {user: points}
        else:
            if user not in contests[contest]:
                contests[contest][user] = points
            else:
                if contests[contest][user] < points:
                    contests[contest][user] = points

for contest, info in contests.items():
    print(f"{contest}: {len(info)} participants")
    sorted_info = sorted(info.items(), key=lambda x: (-x[1], x[0]))
    for participant in sorted_info:
        print(f"{sorted_info.index(participant)+1}. {participant[0]} <::> {participant[1]}")

participants = {}

for value in contests.values():
    for k, v in value.items():
        if k not in participants:
            participants[k] = v
        else:
            participants[k] += v

sorted_participants = sorted(participants.items(), key=lambda x: (-x[1], x[0]))

print("Individual standings:")
for participant in sorted_participants:
    print(f"{sorted_participants.index(participant)+1}. {participant[0]} -> {participant[1]}")
