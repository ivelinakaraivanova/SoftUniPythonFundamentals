persons = int(input())
days = int(input())

coins = 0

for day in range(1,days+1):
    if day % 10 == 0:
        persons -= 2

    if day % 15 == 0:
        persons += 5
        coins -= persons * 2

    coins += 50 - persons * 2

    if day % 3 == 0:
        coins -= persons * 3

    if day % 5 == 0:
        coins += persons * 20


print(f"{persons} companions received {int(coins/persons)} coins each.")
