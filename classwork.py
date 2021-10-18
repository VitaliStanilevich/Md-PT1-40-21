l = 'five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'.split( )
d = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10, 'eleven':11, 'twelve':12, 'thirteen':13, 'fourteen':14, 'fifteen':15, 'sixteen':16, 'seventeen':17, 'eighteen':18, 'nineteen':19, 'twenty':20}
l = [d[i] for i in l if i in d]

l = list(set(l))
print(l)

l=sorted(l)

new_list = []
for i in range(len(l)-1):
    if i%2 == 0:
        new_list.append(l[i]+l[i+1])
    else:
        new_list.append(l[i]*l[i+1])
print(new_list)


sum = 0
for i in range(len(l)-1):
    if l[i]%2 != 0:
        sum += l[i]
print(sum)






