input_strings = list(map(int, input().split(", ")))

even_numbers_indices = [index for index in range(len(input_strings)) if input_strings[index] % 2 == 0]

print(even_numbers_indices)