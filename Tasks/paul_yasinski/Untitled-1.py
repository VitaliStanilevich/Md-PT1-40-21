a = input("Введите число a")
if a==0:
    print("Это не квадратное уравнение.")
b = input("Введите число b")
c = input("Введите число c")
D = (b**2)-(4*c*a)
x1 = (-b-Math.sqrt(D))/(2*a)
x2 = (-b+Math.sqrt(D))/(2*a)
if D>0:
    print("Первый корень: " + x1)
    print("Второй корень: " + x2)
elif D<0:
    print("Корней нет")
else:
    print("Единственный корень: " + x2)