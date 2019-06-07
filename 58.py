import math

def corners(dimension):
    return [dimension ** 2, dimension ** 2 - dimension + 1, dimension ** 2 - (2 * (dimension - 1)), dimension ** 2 - (3 * (dimension - 1))]

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


def find_side_length():
    corner_count = 1
    prime_count = 0
    ratio =  1
    dimension = 1
    primes = all_primes_under(500000)
    while ratio > 0.1:
        dimension += 2
        new_corners = corners(dimension)
        for num in new_corners:
            if is_prime(num, primes):
                prime_count += 1
        corner_count += 4
        ratio = prime_count / float(corner_count)
    return dimension

def is_prime(num, divisors):
  for possible_divisor in divisors:
    if num % possible_divisor == 0:
      return False
    if possible_divisor > math.sqrt(num):
      return True
