from math import sqrt #импортируем из модуля math квадратный корень 
a, b, c = int(input()), int(input()), int(input()) 

D = b ** 2 - 4 * a * c #находим дискриминант
if D > 0: #условие если дискриминант больше 0
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print('Два корня', x1, x2)
elif D == 0: #условие если дискриминант меньше 0
    x = -b / (2 * a)
    print('Один корень', x)
else:
    print("Корней нет")






 

