key = int(input())
n = int(input())

message = ""

for i in range(n):
    char = input()
    new_char = (chr(ord(char)+key))
    message += new_char

print(message)