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

primes = set(all_primes_under(1000000))

def num_consecutive_primes(a,b):
    result = 0
    for n in range(1000):
        if is_prime(pow(n, 2) + (a * n) + b):
            result = result + 1
        else:
            break
    return result


def is_prime(n):
    return n in primes 

best_consecutive_primes = 0
best_a = None
best_b = None
primes_under_1000 = all_primes_under(1000)
possible_b_values = primes_under_1000 + map(lambda x: -x, primes_under_1000) 
for a in range(-1000,1000):
    for b in possible_b_values:
        consecutive_primes = num_consecutive_primes(a,b)
        if consecutive_primes > best_consecutive_primes:
            best_a = a
            best_b = b
            best_consecutive_primes = consecutive_primes

print best_a * best_b