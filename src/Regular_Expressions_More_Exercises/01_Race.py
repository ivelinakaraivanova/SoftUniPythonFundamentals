import re

participants = input().split(", ")
racers = {}

pattern = r'[a-zA-Z0-9]+'

while True:
    text = input()
    if text == "end of race":
        break
    match = re.findall(pattern, text)
    string = "".join(match)
    name = ''
    distance = 0
    for s in string:
        if s.isalpha():
            name += s
        else:
            distance += int(s)
    if name in participants:
        if name not in racers:
            racers[name] = distance
        else:
            racers[name] += distance

sorted_racers = sorted(racers.items(), key=lambda x: -x[1])
racers_for_print = sorted_racers[:3]

print(f"1st place: {racers_for_print[0][0]}")
print(f"2nd place: {racers_for_print[1][0]}")
print(f"3rd place: {racers_for_print[2][0]}")

