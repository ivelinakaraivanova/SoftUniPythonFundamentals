students = {}

n= int(input())

for _ in range(n):
    student_name = input()
    grade = float(input())
    if student_name not in students:
        students[student_name] = [grade]
    else:
        students[student_name].append(grade)

above_average = {}

for student, grades in students.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.5:
        above_average[student] = average_grade

sorted_average = sorted(above_average.items(), key=lambda x: -x[1])

for student, average in sorted_average:
    print(f"{student} -> {average:.2f}")
