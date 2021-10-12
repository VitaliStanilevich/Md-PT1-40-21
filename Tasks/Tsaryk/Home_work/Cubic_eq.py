import math
import cmath

# a = int(input())
# b = int(input())
# c = int(input())
# D = b**2 - 4 * a * c
# if D < 0:
#     print("Решений нет")
# elif D == 0:
#     x = (-b) / (2 * a)
#     print("Т.к. дискриминант равен 0, ответ равен: ", x)
# else:
#     x1 = (-b - D**(0.5))/(2 * a)
#     x2 = (-b + D**(0.5))/(2 * a)
#     print("В решении два ответа: ", x1, x2)

#Попытка №4
# ax3+bx2+cx+d=0
print("Решение кубического уравнения вида: 'ax3+bx2+cx+d=0'")
a = int(input("Введите значение переменной а "))
b = int(input("Введите значение переменной b "))
c = int(input("Введите значение переменной c "))
d = int(input("Введите значение переменной d "))
n = int(input("Степень округления n "))
p = -b**2 / (3 * a**2) + c/a
q = (2 * b**3)/(27 * a**3) - (b * c) / (3 * a**2) + d/a
Q = (p/3)**3 + (q/2)**2
R = (2 * (a ** 3) - 9 * a * b + 27 * c) / 54
S = Q ** 3 - R ** 2
if S>0:
    phi = math.acos((R / ((Q ** 3) ** 0.5))) / 3
    x1 = round( -2 * math.sqrt(Q) * math.cos(phi) - a / 3,n)
    x2 = round( -2 * math.sqrt(Q) * math.cos(phi + 2 * math.pi / 3) - a / 3,n)
    x3 = round( -2 * math.sqrt(Q) * math.cos(phi - 2 * math.pi / 3) - a / 3,n)
    print("Т.к. S > 0, функция имеет три действительных корня и они равны: \n x1 =", x1,'\n x2 =', x2,'\n x3 =', x3)
elif S < 0:
    if Q > 0:
        A = (-q / 2 + math.sqrt(Q)) ** (1 / 3)
        B = (-1)*(q/2 + math.sqrt(Q)) ** (1 / 3)
        x1 = round(A+B - b/(3 * a),n)
        x2 = round(-(A+B)/2 - b/(3 * a),n) + 1j*round((A-B)*math.sqrt(3)/2,n)
        x3 = round(-(A+B)/2 - b/(3 * a),n) - 1j*round((A-B)*math.sqrt(3)/2,n)
        print("Функция имеет один действительнй корень и два комплексных и они равны: \n x1 =", x1,'\n x2 =', x2,'\n x3 =', x3)
    elif Q < 0:
        phi = cmath.atan(-2 * cmath.sqrt(-Q) / q) + cmath.pi
        x1 = 2 * math.sqrt(-p / 3) * cmath.cos(phi / 3) - b / (3 * a)
        x2 = 2 * math.sqrt(-p / 3) * cmath.cos((phi / 3) + 2 * cmath.pi / 3) - b / (3 * a)
        x3 = 2 * math.sqrt(-p / 3) * cmath.cos((phi / 3) + 4 * cmath.pi / 3) - b / (3 * a)
        x1 = round(x1.real,n)
        x2 = round(x2.real,n)
        x3 = round(x3.real,n)
        print("Функция имеет три действительных корня и они равны: \n x1 =", x1,'\n x2 =', x2,'\n x3 =', x3)
    else:
        A = (-q / 2 + math.sqrt(Q)) ** (1 / 3)
        B = (-1)*(q/2 + math.sqrt(Q)) ** (1 / 3)
        x1 = round(A+B - b/(3 * a),n)
        x2 = round(-(A+B)/2 - b/(3 * a),n) + 1j*round((A-B)*math.sqrt(3)/2,n)
        x3 = round(-(A+B)/2 - b/(3 * a),n) - 1j*round((A-B)*math.sqrt(3)/2,n)
        print("Функция имеет один действительнй корень и два комплексных и они равны: \n x1 =", x1,'\n x2 =', x2,'\n x3 =', x3)

#
# #Попытка №3
# print("Решение кубического уравнения вида: 'ax3+bx2+cx+d=0'")
# a = int(input("Введите значение переменной а "))
# b = int(input("Введите значение переменной b "))
# c = int(input("Введите значение переменной c "))
# d = int(input("Введите значение переменной d "))
#
# s1 = b/a
# s2 = c/a
# s3 = d/a
# p = -(s1**2)/3 + s2
# q = 2*(s1**3)/27 - (s1*s2)/3 + s3
# y = ((-1*q/2 + math.sqrt(((q**2)/4)+(p**3)/27))**(1/3))+((-1*q/2 + math.sqrt(((q**2)/4)-(p**3)/27))**(1/3))
#
#
# # Попытка №2 - Метод с Википедии (считает увы не правильно)
# # ax3+bx2+cx+d=0 -
# print("Решение кубического уравнения вида: 'ax3+bx2+cx+d=0'")
# a = int(input("Введите значение переменной а "))
# b = int(input("Введите значение переменной b "))
# c = int(input("Введите значение переменной c "))
# d = int(input("Введите значение переменной d "))
# # #p = c/a - b/(a**2)
# # #q = ((-3*b*c/(a**2))*(2*(b**3)/(a**3)) + d/a)/2
# p = (3 * a * c - b ** 2) / (27 * (a ** 3))
# q = (2 * (b ** 3) - 9 * a * b * c + 27 * (a ** 2) * d) / (27 * (a ** 3))
# D = (p / 3) ** 3 + (q / 2) ** 2
# A = (-q / 2 + (D) ** (0.5)) ** (1 / 3)
# B = (-q / 2 - (D) ** (0.5)) ** (1 / 3)
# y1 = (A + B).real
# y2 = -(A + B) / 2 + ((A - B) / 2) * (3 ** 0.5) * 1j
# y3 = -(A + B) / 2 - ((A - B) / 2) * (3 ** 0.5) * 1j
# x1 = y1 - b / (3 * a)
# x2 = y2 - b / (3 * a)
# x3 = y3 - b / (3 * a)
# print(x1, x2, x3)
#
# #Попытка №1 Тригонометрическая формула Виета - аналогично не выдаёт корректного ответа
# print("Решение кубического уравнения вида: 'ax3+bx2+cx+d=0'")
# a = int(input("Введите значение переменной а "))
# b = int(input("Введите значение переменной b "))
# c = int(input("Введите значение переменной c "))
# d = int(input("Введите значение переменной d "))
# Q = (a ** 2 - 3 * b) / 9
# R = (2 * (a ** 3) - 9 * a * b + 27 * c) / 54
# S = Q ** 3 - R ** 2
# if S > 0:
#     phi = math.acos((R / ((Q ** 3) ** 0.5))) / 3
#     x1 = -2 * math.sqrt(Q) * math.cos(phi) - a / 3
#     x2 = -2 * math.sqrt(Q) * math.cos(phi + 2 * math.pi / 3) - a / 3
#     x3 = -2 * math.sqrt(Q) * math.cos(phi - 2 * math.pi / 3) - a / 3
#     print("Т.к. S > 0, функция имеет три действительных корня и они равны: ", x1, x2, x3, Q, R, S)
# elif S < 0:
#     if Q > 0:
#         phi = math.acosh((math.fabs(R) / ((Q ** 3) ** 0.5))) / 3
#         x1 = -2 * math.fabs(R) * math.sqrt(Q) * math.cosh(phi) - a / 3
#         x2 = math.fabs(R) * math.sqrt(Q) * math.cosh(phi) - a / 3 + math.sqrt(3) * math.sqrt(Q) * math.sinh(phi) * 1j
#         x3 = math.fabs(R) * math.sqrt(Q) * math.cosh(phi) - a / 3 - math.sqrt(3) * math.sqrt(Q) * math.sinh(phi) * 1j
#         print("Т.к. S < 0, а Q > 0, то функция имеет один действительный корень и два комплексных: ", x1, x2, x3, Q, R,
#               S)
#     elif Q < 0:
#         phi = math.asinh((math.fabs(R) / ((math.fabs(Q) ** 3) ** 0.5))) / 3
#         x1 = -2 * math.copysign(R,0) * math.sqrt(math.fabs(Q)) * cmath.sinh(phi) - a / 3
#         x2 = math.copysign(R,0) * math.sqrt(math.fabs(Q)) * cmath.sinh(phi) - a / 3 + math.sqrt(3) * math.sqrt(
#             math.fabs(Q)) * cmath.cosh(phi) * 1j
#         x3 = math.copysign(R,0) * math.sqrt(math.fabs(Q)) * cmath.sinh(phi) - a / 3 - math.sqrt(3) * math.sqrt(
#             math.fabs(Q)) * cmath.cosh(phi) * 1j
#         print("Т.к. S < 0, а Q < 0, то функция имеет один действительный корень и два комплексных: ", x1, x2, x3, Q, R,
#               S)
#     else:
#         x1 = -(c - ((a ** 3) / 27) ** (1 / 3)) - a / 3
#         x2 = -(a + x1) / 2 + (math.sqrt(math.fabs((a - 3 * x1) * (a + x1) - 4 * b)) * 1j) / 2
#         x3 = -(a + x1) / 2 - (math.sqrt(math.fabs((a - 3 * x1) * (a + x1) - 4 * b)) * 1j) / 2
#         print("Т.к. S < 0, а Q = 0, то функция имеет один действительный корень и два комплексных: ", x1, x2, x3, Q, R,
#               S)
#
# # else:
# #   x1 = -2 * (R ** (1 / 3) - a / 3
# #   x2 = R ** (1 / 3) - a / 3
# #   print("Т.к. S > 0, функция имеет три действительных корня и они равны: ", x1,x2,x3)
