def reverse(num):
  return int(str(num)[::-1])

def all_odd_digits(num):
  while num > 0:
      if num % 2 == 0:
          return False
      else:
         num /= 10
  return True

def is_reversible(n):
  if n % 10 == 0:
    return False
  reversed_number = reverse(n)
  if reversed_number % 2 == 0 and n % 2 == 0 or reversed_number % 2 == 1 and n % 2 == 1:
      return False
  else:
    return all_odd_digits(n + reversed_number)

def reversible_numbers_under_n(n):
  count = 0
  for i in range(n):
    if is_reversible(i):
      count +=  1
  return count
