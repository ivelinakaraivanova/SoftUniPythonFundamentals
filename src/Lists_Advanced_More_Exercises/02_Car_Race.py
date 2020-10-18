def left_car(data_list):
    half_len = len(data_list) // 2
    time = 0
    for i in range(half_len):
        time += int(data_list[i])
        if int(data_list[i]) == 0:
            time -= time * 0.2
    return time


def right_car(data_list):
    half_len = len(data_list) // 2
    time = 0
    for i in range(len(data_list)-1, half_len, -1):
        time += int(data_list[i])
        if int(data_list[i]) == 0:
            time -= time * 0.2
    return time


def winner_car(left, right):
    if left <= right:
        return 'left', left
    elif left > right:
        return 'right', right


times = input().split()

winner = winner_car(left_car(times), right_car(times))[0]
winner_time = winner_car(left_car(times), right_car(times))[1]

print(f"The winner is {winner} with total time: {winner_time:.1f}")