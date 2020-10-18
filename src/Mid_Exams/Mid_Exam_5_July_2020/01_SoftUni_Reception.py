first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
students_count = int(input())

time = 0

productivity = first_employee + second_employee + third_employee
whole = students_count // productivity
residue = students_count % productivity
if residue != 0:
    whole += 1

time = whole + (whole // 3)
if (whole > 0) and (whole % 3 == 0):
    time -= 1

print(f"Time needed: {time}h.")