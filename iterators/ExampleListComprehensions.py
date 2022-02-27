#!/usr/bin/env python

print("List comprehensions example")

# =====================================================================
# The classic way of creating a list
squares = []
for i in range(10):
    # squares.append(i**2)
    squares.append(i * i)
print(f'squares: {squares}')

# Here is the list comprehensions version
# new_list = [expression for member in iterable]
squares_lc = [i*i for i in range(10)]
print(f'squares_lc: {squares_lc}')

# =====================================================================
# Using map function
tax_nums = [1.83, 348.28, 34.34, 34771.23, 38471.33]
print(f'Before tax: {tax_nums}')
tax_rate = 0.25


def price_with_tax(price):
    return price * (1 + tax_rate)


# Note: use list constructor to the output of map()
final_prices = list(map(price_with_tax, tax_nums))
print(f'After tax: {final_prices}')

# List comprehensions version
final_prices_lc = [price_with_tax(price) for price in tax_nums]
print(f'After tax LC: {final_prices_lc}')
# =====================================================================
