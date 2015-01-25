def next_lexicographic_permutation(arr):
    # http://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
    if arr ==  sorted(arr)[::-1]:
        return None
    else:
        k = find_k(arr)
        l = find_l(arr, k) 
        arr = switch_indices(arr, k, l)
        arr = arr[:k+1] + list(reversed(arr[k+1:]))
        return arr

def find_k(arr):
    for i in reversed(range(len(arr) - 1)):
        if arr[i] < arr[i + 1]:
            return i

def find_l(arr, k):
    for i in reversed(range(k + 1, len(arr))):
        if arr[k] < arr[i]:
            return i

def switch_indices(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp
    return arr

def nth_lexicographic_permutation(arr, n):
    result = sorted(arr)
    for i in range(n - 1):
        result = next_lexicographic_permutation(result)
    return result

print nth_lexicographic_permutation([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1000000)