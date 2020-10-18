def find_palindrome(input_list):
    palindromes = []
    for item in input_list:
        if item == item[::-1]:
            palindromes.append(item)
    return palindromes


input_data = input().split()
searched_word = input()

palindrome_list = find_palindrome(input_data)
print(palindrome_list)

count = palindrome_list.count(searched_word)
print(f"Found palindrome {count} times")