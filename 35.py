import math

def all_primes_under(num):
    all_primes = []
    for i in range(2, num):
        is_prime = True
        for possible_divisor in all_primes:
            if i % possible_divisor == 0:
                is_prime = False
                break
            if possible_divisor > math.sqrt(i):
                break
        if is_prime == True:
            all_primes.append(i)
    return all_primes

def circular_primes_under(num):
    all_primes = set(all_primes_under(num))
    circular_primes = set()
    for prime in all_primes:
        rotations = set(all_rotations(prime))
        if rotations.issubset(all_primes):
            circular_primes = circular_primes.union(rotations)
    return circular_primes

def all_rotations(num):
    stringified = str(num)
    result = []
    for i in range(len(stringified)):
        result.append(int(stringified))
        stringified = rotate(stringified)
    return result

def rotate(s):
    return s[1:] + s[0]

print len(circular_primes_under(1000000))