n = int(input())
word = input()

string_list =[]
with_word = []

for i in range(n):
    input_string = input()
    string_list.append(input_string)
    if word in input_string:
        with_word.append(input_string)

print(string_list)
print(with_word)