#quadratic equation
# ax**2+bx+c=0
# 3x**2 - 14x-5=0
a=3
b=-14
c=-5
d = (b ** 2) - (4 * a * c)
if d > 0:
 x1 = (-b + d**0.5)/ (2*a)
 print('x1=',x1)
 x2 = (-b - d**0.5)/ (2*a)
 print('x2=',x2)
elif d == 0:
    x = -b/ (2 * a)
    print(x)
else :
    print('нет корней')
