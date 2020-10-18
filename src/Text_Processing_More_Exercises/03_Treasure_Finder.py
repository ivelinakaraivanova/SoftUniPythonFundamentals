def decrypt_string(strng, lst):
    res_string = ''
    pos = 0
    for i in range(len(strng)):
        res_string += chr(ord(strng[i]) - lst[pos])
        pos += 1
        if pos == len(lst):
            pos = 0
    return res_string


def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


def get_type(strng, ch):
    start_index = find(strng, ch)[0]
    stop_index = find(strng, ch)[1]
    res_str = strng[start_index+1:stop_index]
    return res_str


def get_coordinates(strng, ch1, ch2):
    start_index = strng.index(ch1)
    stop_index = strng.index(ch2)
    res_str = strng[start_index+1:stop_index]
    return res_str


key = list(map(int, input().split()))

while True:
    string = input()
    if string == "find":
        break
    else:
        decrypted_string = decrypt_string(string, key)
        treasure_type = get_type(decrypted_string, "&")
        treasure_coordinates = get_coordinates(decrypted_string, "<", ">")
        print(f"Found {treasure_type} at {treasure_coordinates}")
