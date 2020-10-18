def find_len_diff(str1, str2):
    if len(str1) <= len(str2):
        result = str2[len(str1):]
    else:
        result = str1[len(str2):]
    return result


def multiplied_codes(str1, str2):
    result = 0
    zipped = list(zip(str1, str2))
    for pair in zipped:
        ord1 = ord(pair[0])
        ord2 = ord(pair[1])
        prod = ord1 * ord2
        result += prod
    return result


def sum_ords(string):
    return sum([ord(x) for x in string])


first, second = input().split()

result = multiplied_codes(first, second) + sum_ords(find_len_diff(first, second))
print(result)
