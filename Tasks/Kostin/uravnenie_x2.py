
import math
print("введите данные")
a=int(input())
b=int(input())
c=int(input())

discr = b**2-4*a*c

print (discr)

if discr>0:

    x1=(-b+math.sqrt(discr))/(2*a)

    x2=(-b-math.sqrt(discr))/(2*a)

    print( x1,x2)

elif discr==0:
    x3=-b/(2*a)
    print(x3)
else:
    print("нет корней")
2