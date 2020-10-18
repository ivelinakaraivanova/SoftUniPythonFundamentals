def loading_bar(number):
    symbols = int(number / 10)
    if 0 <= number <= 90:
        print(f"{number}% ["+"%"*symbols+"."*(10-symbols)+"]")
        print("Still loading...")
    else:
        print("100% Complete!")
        print("[%%%%%%%%%%]")


num = int(input())
loading_bar(num)