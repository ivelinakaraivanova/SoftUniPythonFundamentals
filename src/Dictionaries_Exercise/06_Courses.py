courses = {}

while True:
    input_line = input()
    if input_line == "end":
        break
    else:
        split_line = input_line.split(" : ")
        course_name = split_line[0]
        student_name = split_line[1]
        if course_name not in courses:
            courses[course_name] = [student_name]
        else:
            courses[course_name].append(student_name)

sorted_courses = sorted(courses.items(), key=lambda x: (-len(x[1])))

for c in sorted_courses:
    print(f"{c[0]}: {len(c[1])}")
    for s in sorted(c[1]):
        print(f"-- {s}")