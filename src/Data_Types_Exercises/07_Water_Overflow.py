n = int(input())

tank_capacity = 255

for row in range(1,n+1):
    water = int(input())
    tank_capacity -= water
    if tank_capacity < 0:
        print("Insufficient capacity!")
        tank_capacity += water

print(f"{255 - tank_capacity}")

"""
total_liters = 0
for i in range(n):
    liters = int(input())
    if total_liters + liters > capacity:
        print("Insufficient capacity!")
    else:
        total_liters += liters
print(total_liters)
"""