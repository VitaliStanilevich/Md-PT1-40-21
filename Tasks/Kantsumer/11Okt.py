f = input("Введите yравнение 'y=kx+b' ")
x = float(input("введите x"))
a = f.split("x") 
d = float (a[0][2:])
b = float (a[1])
y = d * x + b
print(y)