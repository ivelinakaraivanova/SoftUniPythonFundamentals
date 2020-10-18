def is_perfect(number):
    divisors_list = []
    int_num = int(number)
    if int_num > 0:
        for d in range(1, int_num//2+1):
            if int_num % d == 0:
                divisors_list.append(d)
    if int_num == sum(divisors_list):
        return True
    else:
        return False


input_data = input()
if is_perfect(input_data):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
