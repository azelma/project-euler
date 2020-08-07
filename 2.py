def sumOfEvenFibs(n):
  terms = [1, 1, 2]
  total = 0
  while terms[2] <= n:
    total += terms[2]
    t0 = terms[1] +  terms[2]
    t1 = terms[2] + t0
    terms = [t0, t1, t0 + t1]
  return total

print(sumOfEvenFibs(4000000))
