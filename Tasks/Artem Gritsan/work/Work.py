l = 'five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'
k = {
    'one': 1,
    'two': 2,
    'four': 4,
    'five': 5,
    'eight': 8,
    'thirteen': 13,
    'eleven': 11,
    'seventeen': 17,
    'ten': 10,
    'nineteen': 19
}
l = l.split()

for i in range(len(l)):
    l[i] = k[l[i]]
l = sorted(set(l))
l = list(l)
for x in range(len(l)):
    if x % 2 == 0:
        l[x] = l[x] * l[x+1]
    else:
        if x != len(l) - 1:
            l[x] = l[x] + l[x+1]
print(l)
p = 0
for y in l:
    if y % 2 != 0:
        p += y
print(p)