def display_even_numbers(start, end):
    show = ', '.join([str(digit) for digit in range(start, end) if digit % 2 == 0])
    return print(show)

display_even_numbers(1, 20)