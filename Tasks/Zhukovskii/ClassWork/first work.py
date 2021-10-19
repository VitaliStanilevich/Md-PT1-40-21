l = input("Input digts: ") 
from operator import itemgetter
d = {'one': 1, 'two': 2, 'three':3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelfth': 12, 'thirteen': 13, 'forteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20}
#t = "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen".split ( )
print("Your dights: ",itemgetter(*l.split())(d))
z = list(set(itemgetter(*l.split())(d)))
print("sorted:", z)
l = len(z)
i = 0
while i < l:
    p = z[i]*z[i+1]
    i +=2
    print("product =",p)
i = 1
while i < l-1:
    s = z[i]+z[i+1]
    i +=2
    print("sum =", s)
S = 0
for i in range (l):
    if z[i]%2==1:
        S +=z[i]
print("sum odd =", S)