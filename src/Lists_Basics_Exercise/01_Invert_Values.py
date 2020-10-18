input_list = input()

split_list = input_list.split(" ")
inverted_list = []
for el in split_list:
    opposite_el = -int(el)
    inverted_list.append(opposite_el)
print(inverted_list)