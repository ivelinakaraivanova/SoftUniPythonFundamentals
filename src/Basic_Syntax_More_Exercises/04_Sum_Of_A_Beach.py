input_string = input().lower()

count = 0

for word in ["water", "sand", "fish", "sun"]:
    if word in input_string:
        count += input_string.count(word)

print(count)