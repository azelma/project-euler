import math

products = set()

def is_pandigital(multiplicand, multiplier):
    product = multiplicand * multiplier
    digit_string = str(product) + str(multiplicand) + str(multiplier)
    digit_string = ''.join(sorted(digit_string))
    return digit_string == '123456789'

for i in range(1, 100):
    for j in range(1, 10000):
        if is_pandigital(i, j):
            products.add(i * j)

print sum(products)