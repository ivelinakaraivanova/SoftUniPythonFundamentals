import re

pattern = r'U\$(?P<username>[A-Z][a-z]{2,})U\$P@\$(?P<password>[a-zA-Z]{5,}[0-9]+)P@\$'

n = int(input())
count = 0
for _ in range(n):
    text = input()
    if re.search(pattern, text) is not None:
        matches = re.finditer(pattern, text)
        for match in matches:
            username = match.group('username')
            password = match.group('password')
            print("Registration was successful")
            print(f"Username: {username}, Password: {password}")
            count += 1
    else:
        print("Invalid username or password")

print(f"Successful registrations: {count}")