l = [10,1,1,6,5,4543,8,2,2,4,7,9]

for i in range(len(l)-1):
    m = i
    j = i+1
    while j < len(l):
        if l[j]<l[m]:
            m = j
        j += 1
    l[i], l[m] = l[m], l[i]

print(l)   