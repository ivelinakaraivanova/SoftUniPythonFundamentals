faro_cards = input().split(" ")
shuffle = int(input())

old_list = faro_cards

half_length = len(faro_cards)//2
for s in range(shuffle):
    new_list = []
    for i in range(len(old_list)//2):
        even_element = old_list[i]
        odd_element = old_list[half_length+i]
        new_list.append(even_element)
        new_list.append(odd_element)
    old_list = new_list

print(old_list)