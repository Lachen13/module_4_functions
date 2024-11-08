def is_palindrome(number):
    number = str(number)

    num_1 = [int(num) for num in number[3:]]
    num_2 = [int(num) for num in number[:3]]

    return sum(num_1) == sum(num_2)

print(is_palindrome(546645))
print()
print(is_palindrome(421987))