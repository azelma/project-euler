def sum_of_proper_divisors(n):
    sum = 0
    for i in range(1, int(n/2) + 1):
        if n % i == 0:
            sum = sum + i
    return sum

def is_abundant(n):
    return sum_of_proper_divisors(n) > n

def all_abundant_numbers_below(n):
    result = []
    for i in range(12,n):
        if is_abundant(i):
            result.append(i)
    return result

abundant_numbers = all_abundant_numbers_below(28123)
can_sum = set()
for i in range(len(abundant_numbers)):
    for j in range(i, len(abundant_numbers)):
        current_sum = abundant_numbers[i] + abundant_numbers[j]
        if current_sum < 28123:
            can_sum.add(current_sum)

print sum(range(28123)) - sum(can_sum)