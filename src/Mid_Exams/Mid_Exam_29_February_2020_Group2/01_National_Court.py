first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
people_count = int(input())

time = 0

total_time = first_employee + second_employee + third_employee
whole = people_count // total_time
residue = people_count % total_time
if residue != 0:
    whole += 1

time = whole + (whole // 3)
if (whole > 0) and (whole % 3 == 0):
    time -= 1


print(f"Time needed: {time}h.")
