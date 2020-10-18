def gladiator_stance(string):
    return string.upper()


def defensive_stance(string):
    return string.lower()


def dispel(string, ind, new_letter):
    if 0 <= ind < len(string):
        string = string[:ind] + new_letter + string[ind+1:]
        return string
    else:
        return -1


def target_change(string, first, second):
    if first in string:
        string = string.replace(first, second)
    return string


def target_remove(string, substr):
    if substr in string:
        string = string.replace(substr, '')
    return string


text = input()

while True:
    data = input()
    if data == "For Azeroth":
        break
    split_data = data.split()
    command = split_data[0]

    if command == "GladiatorStance":
        text = gladiator_stance(text)
        print(text)

    elif command == "DefensiveStance":
        text = defensive_stance(text)
        print(text)

    elif command == "Dispel":
        index = int(split_data[1])
        letter = split_data[2]
        if dispel(text, index, letter) != -1:
            text = dispel(text, index, letter)
            print("Success!")
        else:
            print("Dispel too weak.")

    elif command == "Target" and split_data[1] == "Change":
        first_string = split_data[2]
        second_string = split_data[3]
        text = target_change(text, first_string, second_string)
        print(text)

    elif command == "Target" and split_data[1] == "Remove":
        substring = split_data[2]
        text = target_remove(text, substring)
        print(text)

    else:
        print("Command doesn't exist!")
