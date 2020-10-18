targets = list(map(int, input().split()))

shots_count = 0

while True:
    input_line = input()
    if input_line == "End":
        print(f"Shot targets: {shots_count} -> {' '.join(list(map(str, targets)))}")
        break
    else:
        index = int(input_line)
        if index in range(len(targets)):
            if targets[index] != -1:
                for i in range(len(targets)):
                    if targets[i] != -1:
                        if i != index:
                            if targets[i] > targets[index]:
                                targets[i] -= targets[index]
                            else:
                                targets[i] += targets[index]
                targets[index] = -1
                shots_count += 1
