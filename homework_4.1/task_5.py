def product_numbers(start, end):
    if start > end:
        start, end = end, start

    product = 1
    for num in range(start, end + 1): # end включительно
        product *= num

    return product


print(product_numbers(5, 3))