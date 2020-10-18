def sum_digits(string):
    list_digits = [int(d) for d in string]
    return sum(list_digits)


def get_element(text, number):
    index = number % len(text)
    return index


input_string_digits = input().split(" ")
message = input()

output_string = ""

sums_list = [sum_digits(number) for number in input_string_digits]

for s in sums_list:
    output_string += message[get_element(message, s)]
    message = message[0:get_element(message, s)] + message[get_element(message,s)+1:len(message)]


print(output_string)