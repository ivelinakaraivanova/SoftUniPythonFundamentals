year = int(input())

for i in range(year+1, 10000):
    new_string = ""
    for c in str(i):
        if c not in new_string:
            new_string += c
    if len(str(i)) == len(new_string):
        print(i)
        break


"""        
d = year % 10
year = (year - d) // 10
c = year % 10
year = (year - c) // 10
b = year % 10
year = (year - b) // 10
a = year % 10
"""


