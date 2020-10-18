while True:
    word = input()
    if word == "end":
        break
    else:
        reversed_word = word[::-1]
        print(f"{word} = {reversed_word}")
