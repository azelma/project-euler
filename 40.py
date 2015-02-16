def string_of_positive_integers_of_min_length(length):
    result = ""
    i = 1
    while len(result) < length:
        result = result + str(i)
        i = i + 1
    return result

s = string_of_positive_integers_of_min_length(1000000)
print int(s[0]) * int(s[9]) * int(s[99]) * int(s[999]) * int(s[9999]) * int(s[99999]) * int(s[999999])