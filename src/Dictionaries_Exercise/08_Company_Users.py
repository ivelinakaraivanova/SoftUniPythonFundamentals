companies = {}

while True:
    input_line = input()
    if input_line == "End":
        break
    else:
        split_input = input_line.split(" -> ")
        company = split_input[0]
        employee_id = split_input[1]
        if company not in companies:
            companies[company] = [employee_id]
        else:
            if employee_id not in companies[company]:
                companies[company].append(employee_id)

sorted_companies = sorted(companies.items(), key=lambda x: x[0])

for comp in sorted_companies:
    print(f"{comp[0]}")
    for id in comp[1]:
        print(f"-- {id}")
