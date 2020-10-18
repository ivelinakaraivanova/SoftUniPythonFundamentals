coffee_count = 0
act_lower = ["coding", "dog", "cat", "movie"]
act_upper = ["CODING", "DOG", "CAT", "MOVIE"]
command = input()
is_five = False
while command != "END":

    if command in act_lower:
        coffee_count += 1
    elif command in act_upper:
        coffee_count +=2
    if coffee_count > 5:
        is_five = True
        break
    command = input()

if is_five:
    print("You need extra sleep")
else:
    print(coffee_count)