happiness_list = list(map(int, input().split()))
factor = int(input())
new_list = list(map(lambda x: x*factor, happiness_list))
average_new_list = sum(new_list) / len (new_list)

new_happiness_list = list(filter(lambda x: x >= average_new_list, new_list))

happy_count = len(new_happiness_list)
total_count = len(happiness_list)

if happy_count >= (total_count / 2):
    print(f"Score: {happy_count}/{total_count}. Employees are happy!")
else:
    print(f"Score: {happy_count}/{total_count}. Employees are not happy!")