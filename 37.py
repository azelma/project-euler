import math

def truncations(num):
    stringified = str(num)
    result = set()
    if len(stringified) > 1:
        result.add(num)
        for i in range(1, len(stringified)):
            result.add(int(stringified[:i]))
            result.add(int(stringified[-i:]))
    return result

def is_prime(num, primes_up_to):
    for possible_divisor in primes_up_to:
        if num % possible_divisor == 0:
            return False
        if possible_divisor > math.sqrt(num):
            return True

truncatable_primes = set()
all_primes = [2]
all_primes_set = set(all_primes)
i = 3
while len(truncatable_primes) < 11:
    if is_prime(i, all_primes):
        all_primes.append(i)
        all_primes_set.add(i)
        truncs = truncations(i)
        if len(truncs) > 0 and truncs.issubset(all_primes_set):
            truncatable_primes.add(i)
    i = i + 2

print sum(truncatable_primes)