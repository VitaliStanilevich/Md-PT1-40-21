# "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen"
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

print([d[el] for el in "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen".split()])
print(list(set([d[el] for el in "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen".split()])))
print(sorted([d[el] for el in "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen".split()]))
print([sorted([d[el] for el in "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen".split()])[el] * sorted([d[el] for el in "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen".split()])[el + 1] if el % 2 == 0 else sorted([d[el] for el in "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen".split()])[el] + sorted([d[el] for el in "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen".split()])[el + 1] for el in range(len(sorted([d[el] for el in "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen".split()])) - 1)])
print(sum([el for el in sorted([d[el] for el in "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen".split()]) if el % 2 != 0]))