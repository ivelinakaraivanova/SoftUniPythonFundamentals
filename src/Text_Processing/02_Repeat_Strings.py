data = input().split()
result = ""
for string in data:
    new_str = string * len(string)
    result += new_str

print(result)
