cards = input().split(":")

deck = []

while True:
    input_command = input()
    if input_command == "Ready":
        break
    else:
        split_command = input_command.split()
        command = split_command[0]
        card_name = split_command[1]

        if command == "Add":
            if card_name in cards:
                deck.append(card_name)
            else:
                print("Card not found.")

        elif command == "Insert":
            index = int(split_command[2])
            if index in range(len(deck)):
                if card_name in cards:
                    deck.insert(index, card_name)
                else:
                    print("Error!")
            else:
                print("Error!")

        elif command == "Remove":
            if card_name in deck:
                deck.remove(card_name)
            else:
                print("Card not found.")

        elif command == "Swap":
            card_name2 = split_command[2]
            index1 = deck.index(card_name)
            index2 = deck.index(card_name2)
            deck[index1], deck[index2] = deck[index2], deck[index1]

        elif command == "Shuffle":
            deck = list(reversed(deck))

print(" ".join(deck))