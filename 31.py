def ways_to_make(amt, coins):
    combinations = {}
    combinations[0] = 1
    for num in range(1, amt + 1):
        combinations[num] = 0
    for denomination in coins:
        for num in range(denomination, amt + 1):
            if denomination <= num:
                combinations[num] = combinations[num] + combinations[num - denomination]
    return combinations[amt]

print ways_to_make(200, [1,2,5,10,20,50,100,200])