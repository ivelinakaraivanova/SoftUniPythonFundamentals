string = input().upper()

result_string = ''
rep_str = ''
rep_num = ''

for i in range(len(string)):

    if string[i].isdigit():
        rep_num += string[i]
        if i+1 < len(string) and string[i+1].isdigit():
            rep_num += string[i+1]

        count = int(rep_num)

        if count == 0:
            rep_str = ''
            rep_num = ''
        else:
            for j in range(count):
                result_string += rep_str
                if j == count - 1:
                    rep_str = ''
                    rep_num = ''

    else:
        rep_str += string[i]


print(f"Unique symbols used: {len(set(result_string))}")
print(result_string)
