players = {}
skills = {}

while True:
    data = input()
    if data == "Season end":
        break
    else:
        if "->" in data:
            split_data = data.split(" -> ")
            player = split_data[0]
            position = split_data[1]
            skill = int(split_data[2])

            if player not in players:
                players[player] = {position: skill}
                skills[player] = skill
            else:
                if position not in players[player]:
                    players[player][position] = skill
                    if player not in skills:
                        skills[player] = skill
                    else:
                        skills[player] += skill
                else:
                    if players[player][position] < skill:
                        skills[player] -= players[player][position]
                        players[player][position] = skill
                        skills[player] += skill

        else:
            player1, player2 = data.split(" vs ")
            is_common = False
            if player1 in players and player2 in players:
                for position1 in players[player1]:
                    for position2 in players[player2]:
                        if position1 == position2:
                            is_common = True
                            break
                if is_common:
                    if skills[player1] > skills[player2]:
                        skills.pop(player2)
                        players.pop(player2)
                    elif skills[player1] < skills[player2]:
                        skills.pop(player1)
                        players.pop(player1)

sorted_skills = sorted(skills.items(), key=lambda x: (-x[1], x[0]))

for element in sorted_skills:
    print(f"{element[0]}: {element[1]} skill")
    for k, v in players.items():
        if k == element[0]:
            sorted_v = sorted(v.items(), key=lambda x: (-x[1], x[0]))
            for pos in sorted_v:
                print(f"- {pos[0]} <::> {pos[1]}")

#        skills = {k: sum(v.values()) for k, v in players.items()}
