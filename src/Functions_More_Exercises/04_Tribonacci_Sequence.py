def tribonacci_sequence(number):
    if number == 1:
        tri_list = [1]
    elif number == 2:
        tri_list = [1, 1]
    else:
        tri_list = [0]*number
        tri_list[0] = 1
        tri_list[1] = 1
        tri_list[2] = 2
        for i in range(3, number):
            tri_list[i] = tri_list[i-3] + tri_list[i-2] + tri_list[i-1]

    for i in range(0, number):
        print(tri_list[i], '', end='')


num = int(input())

tribonacci_sequence(num)

