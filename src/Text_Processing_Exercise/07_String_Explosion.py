data = input().split(">")
strength = 0
left_strength = 0

for i in range(len(data)):
    if data[i][0].isdigit():
        strength = int(data[i][0]) + left_strength
        if len(data[i]) >= strength:
            data[i] = data[i][strength:]
        else:
            left_strength = strength - len(data[i])
            data[i] = ""

print(">".join(data))
