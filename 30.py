def sum_of_nth_powers_of_digits(num, power):
    total = 0
    for digit in str(num):
        total = total + pow(int(digit), power)
    return total

def all_fifth_power_sum_numbers_under(num):
    result = []
    for i in range(10, num):
        if i == sum_of_nth_powers_of_digits(i, 5):
            result.append(i)
    return result

# 9^5 * 6 = 354294, upper limit for 6 digit numbers
print sum(all_fifth_power_sum_numbers_under(354295))