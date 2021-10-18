s = "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen"
d = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
    "twenty": 20
    }

l = [d[el] for el in s.split()]
print(l)
print(list(set(l)))

for i in range(len(l)):
    for j in range(len(l) - 1):
        if l[j] > l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]
print(l)

l_new = []
for i in range(len(l) - 1):
    if i % 2 == 0:
        l_new.append(l[i] * l[i + 1])
    else:
        l_new.append(l[i] + l[i + 1])
print(l_new)

print(sum([el for el in l if el % 2 != 0]))