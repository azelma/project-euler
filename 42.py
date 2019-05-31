import string

def alphabetical_sum(word):
  alphabet = string.ascii_uppercase
  sum = 0
  for char in word:
    sum += alphabet.index(char) + 1
  return sum

triangle_numbers = []
for i in range(1, 1000):
    triangle_numbers.append(.5 * i * (i + 1))

triangle_word_count = 0
for word in input:
    if alphabetical_sum(word) in triangle_numbers:
        triangle_word_count += 1

print triangle_word_count
