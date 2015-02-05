def distinct_powers(lower_limit, upper_limit):
    result =  set()
    for i in range(lower_limit, upper_limit + 1):
        for j in range(lower_limit, upper_limit + 1):
            result.add(pow(i, j))
    return result

print len(distinct_powers(2, 100))