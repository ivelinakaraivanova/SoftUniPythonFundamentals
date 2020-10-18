def is_valid_ticked(string):
    return len(string) == 20


def halves(string):
    length = int(len(string) / 2)
    first_half = string[:length]
    second_half = string[length:]
    return first_half, second_half


def num_repetitions(string):
    current_count = 0
    current_symbol = ''
    best_count = 0
    best_symbol = ''
    for s in string:
        if s == current_symbol:
            current_count += 1
        else:
            current_count = 1
            current_symbol = s

        if current_count > best_count:
            best_count = current_count
            best_symbol = current_symbol

    return best_count, best_symbol


data = input().split(", ")
stripped_data = [item.strip() for item in data]

winning_symbols = ['@', '#', '$', '^']

for string in stripped_data:
    if not is_valid_ticked(string):
        print("invalid ticket")
    else:
        first_half = halves(string)[0]
        second_half = halves(string)[1]

        first_half_match_length, first_half_match_symbol = num_repetitions(first_half)
        second_half_match_length, second_half_match_symbol = num_repetitions(second_half)
        match_length = min(first_half_match_length, second_half_match_length)

        if first_half_match_symbol == second_half_match_symbol and \
            first_half_match_symbol in winning_symbols and \
            match_length >= 6:

            if match_length <= 9:
                print(f'ticket "{string}" - {match_length}{first_half_match_symbol}')
            else:
                print(f'ticket "{string}" - {match_length}{first_half_match_symbol} Jackpot!')

        else:
            print(f'ticket "{string}" - no match')
