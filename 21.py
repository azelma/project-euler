import math

amicable_numbers_total = 0

def sum_of_proper_divisors(n):
    sum = 0
    for i in range(1, int(n/2) + 1):
        if n % i == 0:
            sum = sum + i
    return sum

def is_amicable(a):
    b = sum_of_proper_divisors(a)
    return a == sum_of_proper_divisors(b) and a != b

for i in range(10000):
    if is_amicable(i):
        amicable_numbers_total = amicable_numbers_total + i

print amicable_numbers_total