input_string = input()

upper_ind = []

for i in range(0,len(input_string)):
    if input_string[i].isupper():
        upper_ind.append(i)

print(upper_ind)