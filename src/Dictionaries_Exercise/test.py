command = input()

employees = {}

while command != "End":
    id_info = command.split(" -> ")
    company = id_info[0]
    employees_id = id_info[1]

    if company not in employees:
        employees[company] = [employees_id]

    if employees_id not in employees[company]:
        employees[company].append(employees_id)

    command = input()

sorted_employees = dict(sorted(employees.items(), key=lambda c: c[0]))

for key, value in sorted_employees.items():
    print(f"{key}")
    for employees_id in value:
        print(f"-- {employees_id}")