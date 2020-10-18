tanks = input().split(", ")
n = int(input())

for _ in range(n):
    input_command = input().split(", ")
    command = input_command[0]

    if command == "Add":
        tank_name = input_command[1]
        if tank_name in tanks:
            print("Tank is already bought")
        else:
            tanks.append(tank_name)
            print("Tank successfully bought")

    elif command == "Remove":
        tank_name = input_command[1]
        if tank_name in tanks:
            tanks.remove(tank_name)
            print("Tank successfully sold")
        else:
            print("Tank not found")

    elif command == "Remove At":
        index = int(input_command[1])
        if index in range(len(tanks)):
            tanks.pop(index)
            print("Tank successfully sold")
        else:
            print("Index out of range")

    elif command == "Insert":
        index = int(input_command[1])
        tank_name = input_command[2]
        if index in range(len(tanks)):
            if tank_name not in tanks:
                tanks.insert(index, tank_name)
                print("Tank successfully bought")
            else:
                print("Tank is already bought")
        else:
            print("Index out of range")

print(", ".join(tanks))
