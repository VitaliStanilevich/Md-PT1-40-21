l = 'five thirteen two eleven seventeen two one thirteen ten four eight five six six seven'.split( )
#l = input('Enter your list of numbers from 1 to 20:').split( )

#task1
d = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10, 'eleven':11, 'twelve':12, 'thirteen':13, 'fourteen':14, 'fifteen':15, 'sixteen':16, 'seventeen':17, 'eighteen':18, 'nineteen':19, 'twenty':20}
l = [d[i] for i in l if i in d]
print(*l)

#task2
l = list(set(l))
print(*l)

#task3
l=sorted(l)
print(*l)

#task4
for i in range(len(l)-1):
    if i%2 == 0:
        print(l[i]+l[i+1], end=' ')
    else:
        print(l[i]*l[i+1], end=' ')
else:
    print()
    
#task5
print(sum([i for i in l if i%2 != 0]))
