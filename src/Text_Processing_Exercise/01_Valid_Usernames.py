def find_len(string):
    result = 3 <= len(string) <= 16
    return result


def string_contains(string):
    sym = ["-", "_"]
    count = 0
    for s in string:
        if s.isdigit() or s.isalpha() or s in sym:
            count += 1
    result = count == len(string)
    return result


data = input().split(", ")

for username in data:
    if find_len(username) and string_contains(username):
        print(username)
