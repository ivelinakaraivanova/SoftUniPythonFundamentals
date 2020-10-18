grade_input = float(input())


def solve(grade):
    if 2.00 <= grade <= 2.99:
        return "Fail"
    elif 3.00 <= grade <= 3.49:
        return "Poor"
    elif 3.5 <= grade <= 4.49:
        return"Good"
    elif 4.5 <= grade <= 5.49:
        return "Very Good"
    elif 5.5 <= grade <= 6.00:
        return "Excellent"


print(solve(grade_input))