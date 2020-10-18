def find_first_letter(word):
    code = ""
    for s in word:
        if not s.isdigit():
            break
        code += s
    first_char = chr(int(code))
    new_word = word.replace(code, first_char)
    return new_word


def swap_chars(word):
    temp = list(word)
    temp[1], temp[-1] = temp[-1], temp[1]
    return "".join(temp)


input_data = input().split()

messages = []
for item in input_data:
    item = swap_chars(find_first_letter(item))
    messages.append(item)

print(" ".join(messages))


