l = [4,2,6,4,7,9,6,8,0,54,3,6,8,9,5,3]

n = len(l)

for i in range(n):
    for j in range(n-i-1):
        if l[j]>l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]

print(l)