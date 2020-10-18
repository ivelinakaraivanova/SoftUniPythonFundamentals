numbers = list(map(int, input().split()))

while True:
    input_line = input()
    if input_line == "end":
        break

    else:
        split_input = input_line.split()
        command = split_input[0]

        if command == "swap":
            index1 = int(split_input[1])
            index2 = int(split_input[2])
            numbers[index1], numbers[index2] = numbers[index2], numbers[index1]

        elif command == "multiply":
            index1 = int(split_input[1])
            index2 = int(split_input[2])
            numbers[index1] = numbers[index1] * numbers[index2]

        elif command == "decrease":
            numbers = [x-1 for x in numbers]

print(", ".join(list(map(str, numbers))))
