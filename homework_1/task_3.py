def display_square(size, symbol, logical_variable):
    if logical_variable:
        for i in range(size):
            print(size * (symbol + ' '))
    else:
        for i in range(size):
            if i == 0 or i == size - 1:
                print(size * (symbol + ' '))
            else:
                print(symbol + ' ' * (size * 2 - 3) + symbol)

display_square(5, '*', True)
print()
display_square(13, '*', False)