import math

students_count = int(input())
lectures_count = int(input())
additional_bonus = int(input())

max_bonus_points = 0
max_attendances = 0

for student in range(students_count):
    student_attendances = int(input())
    if lectures_count != 0:
        total_bonus = student_attendances / lectures_count * (5 + additional_bonus)
        if total_bonus > max_bonus_points:
            max_bonus_points = total_bonus
            max_attendances = student_attendances

print(f"Max Bonus: {math.ceil(max_bonus_points)}.")
print(f"The student has attended {max_attendances} lectures.")