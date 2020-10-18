def char_range(char1, char2):
    range_ascii = [r for r in range(ord(char1)+1, ord(char2))]
    range_char = [chr(r) for r in range_ascii]
    return " ".join(range_char)


first_char = input()
second_char = input()

print(char_range(first_char, second_char))