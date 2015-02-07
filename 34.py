import math

digit_factorials = []
for i in range(10):
    digit_factorials.append(math.factorial(i))

def factorial_sum(num):
    total = 0
    if num >= 10:
        for digit in str(num):
            total = digit_factorials[int(digit)] + total
    return total

def factorial_sum_numbers_under(num):
    result = []
    for i in range (10, num):
        if factorial_sum(i) == i:
            result.append(i)
    return result

# 9! * 7 = 2540160, conservative upper bound
print sum(factorial_sum_numbers_under(2540161))