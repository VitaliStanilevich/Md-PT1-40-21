l = ['five', 'thirteen', 'two', 'eleven', 'seventeen', 'two', 'one', 'thirteen', 'ten', 'four', 'eight', 'five', 'nineteen' ]

d = { 'one':1,'two':2,'tree':3,'four':4, 'five':5,'six':6, 'seven':7,'eight':8, 'nine':9, 'ten':10, 'eleven':11,'twelve':12,'thirteen':13,  'fourteen':14, 'fifteen':15, 'sixteen':16, 'seventeen':17, 'eighteen':18, 'nineteen':19, 'twenty':20 }

s2 = [d[e] for e in l]

print('список первоначальный',s2)

s2 = list(set(s2))

print('список отсартированный и без повторов',s2)

p1=0
p2=1
while p2 < len(s2):   
 pro=s2[p1]*s2[p2]
 p1=p1+2
 p2=p2+2
 print('произведение по парам',pro)

su1=1
su2=2
while su2 < len(s2):   
 sum=s2[su1]+s2[su2]
 su1=su1+2
 su2=su2+2
 print('сумма по парам',sum)

ma=0 
for n in s2:
    if n % 2 != 0:
        #print(n)
        ma=ma+n
print("сумма всех нечетных",ma)

  




