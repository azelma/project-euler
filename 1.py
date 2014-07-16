def sumOf3or5MultiplesUnder(n):
    total = 0
    for i in range (3, n):
        if n % 3 == 0 or n % 5 == 0:
            total = total + n
    return n

sumOf3or5MultiplesUnder(1000)