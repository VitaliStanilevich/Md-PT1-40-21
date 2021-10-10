import math

a = float(input("Введите а: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))
d = float(input("Введите d: "))

p = (3*a*c - b**2)/(3*a**2)
q = (2*b**3 - 9*a*b*c + 27*a**2*d)/(27*a**3)

Q = (p/3)**3 + (q/2)**2

# y1 = alfa + beta
# y2 = complex(-(alfa + beta)/2 + ((alfa + beta)/2)*3**(1/2))
# y3 = complex(-(alfa + beta)/2 - ((alfa + beta)/2)*3**(1/2))

if Q == p == q == 0:
    y = 0
    x = y - (b/(3*a))
    print("Уравнение имеет трехкратный корень x =")
elif Q == 0:
    alfa = -math.fabs(-q/2 + math.sqrt(Q))**(1/3)
    y1 = 2*alfa
    y2 = -alfa
    x = y1 - (b/(3*a))
    doubleX = y2 - (b/(3*a))
    print("Уравнение имеет 3 корня, 2 из которых совпадают: x1 =" ,x, "; x2, x3 =", doubleX)

else:
    print("Уравнение имеет хотя бы один комплексный корень, нахождение которых не входит в техническое задание")

#проверка: 1,0,-12,16
#проверка2: 1,12,36,32