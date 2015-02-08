def is_palindrome(string):
    return string == string[::-1]

def is_double_base_palindrome(num):
    return is_palindrome(str(num)) and is_palindrome("{0:b}".format(num))

def all_double_base_palindromes_under(num):
    result = []
    for i in range(num):
        if is_double_base_palindrome(i):
            result.append(i)
    return result

print sum(all_double_base_palindromes_under(1000000))