input_string = input()

split_list = input_string.split(", ")

for i in range(len(split_list)):
    if split_list[-1] == "wolf":
        print("Please go away and stop eating my sheep")
        break
    elif split_list[i] == "wolf":
        sheep = len(split_list) - (i + 1)
        print(f"Oi! Sheep number {sheep}! You are about to be eaten by a wolf!")
        break