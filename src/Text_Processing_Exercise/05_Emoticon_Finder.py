def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


input_string = input()
emoticon = ""

for ind in find(input_string, ":"):
    emoticon = input_string[ind:ind+2]
    print(emoticon)
