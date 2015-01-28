import re

f = open("p022_names.txt")
text = f.read()
text = re.sub('"','', text)
names = text.split(',')
alphabet = '_ABCDEFGHIJKLMNOPQRSTUVWXYZ'
names.sort()
names.insert(0, "_")
total_score = 0

for i in range(1, len(names)):
    name =  names[i]
    name_score = 0
    for letter in name:
        name_score = name_score + alphabet.index(letter)
    name_score = name_score * i
    total_score = total_score + name_score

print total_score