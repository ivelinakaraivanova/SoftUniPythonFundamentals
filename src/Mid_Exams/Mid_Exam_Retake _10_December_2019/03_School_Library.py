shelf = input().split("&")

while True:
    command = input()
    if command == "Done":
        print(", ".join(shelf))
        break
    else:
        split_command = command.split(" | ")
        action = split_command[0]

        if action == "Add Book":
            book_name = split_command[1]
            if book_name not in shelf:
                shelf.insert(0, book_name)

        elif action == "Take Book":
            book_name = split_command[1]
            if book_name in shelf:
                shelf.remove(book_name)

        elif action == "Swap Books":
            book1 = split_command[1]
            book2 = split_command[2]
            if book1 in shelf and book2 in shelf:
                index1 = shelf.index(book1)
                index2 = shelf.index(book2)
                shelf[index1], shelf[index2] = shelf[index2], shelf[index1]

        elif action == "Insert Book":
            book_name = split_command[1]
            shelf.append(book_name)

        elif action == "Check Book":
            index = int(split_command[1])
            if index in range(len(shelf)):
                print(shelf[index])
