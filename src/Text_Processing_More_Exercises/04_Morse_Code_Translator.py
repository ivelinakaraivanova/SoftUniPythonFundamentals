morse_sym = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
             ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

alphabet = [chr(s) for s in range(65, 91)]

input_string = input().split("|")

symbols = [s.split() for s in input_string]
result = []

for word in symbols:
    result_word = []
    for symbol in word:
        letter = alphabet[morse_sym.index(symbol)]
        result_word.append(letter)
    words_list = ["".join(result_word)]
    result.append(words_list)

res_list = ["".join(sublist) for sublist in result]
result_string = " ".join(res_list)

print(result_string)

