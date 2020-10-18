rooms_number = int(input())

is_enough = True
free_chairs = 0
for r in range(1, rooms_number+1):
    input_data = input().split()
    chairs = len(input_data[0])
    people = int(input_data[1])
    needed_chairs = 0
    if chairs >= people:
        free_chairs += chairs - people
    else:
        needed_chairs = people - chairs
        print(f"{needed_chairs} more chairs needed in room {r}")
        is_enough = False

if is_enough:
    print(f"Game On, {free_chairs} free chairs left")