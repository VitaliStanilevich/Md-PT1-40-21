import re
from math import *
from numpy import *


#  Addition to the function cubic_equation()
def cub_eq_3(fi, p):
    y1 = 2 * sqrt(- p / 3) * cos(fi / 3)
    y2 = 2 * sqrt(- p / 3) * cos(fi / 3 + (2 * pi / 3))
    y3 = 2 * sqrt(- p / 3) * cos(fi / 3 + (4 * pi / 3))
    return [y1, y2, y3]


# Calculation of the cubic equation. Info from https://ru.intemodino.com/math/algebra/equations/cardano%27s-formula-for-solving-cubic-equations.html
def cubic_equation(a, b, c, d):
    p = (3 * a * c - b ** 2) / (3 * a ** 2)
    q = ((2 * b ** 3) - (9 * a * b * c) + (27 * (a ** 2) * d)) / (27 * a ** 3)
    Q = (q / 2) ** 2 + (p / 3) ** 3
    xy = (b / (3 * a))
    if Q > 0:
        y1 = cbrt(- q / 2 + sqrt(Q)) + cbrt(-q / 2 - sqrt(Q))
        y11 = cbrt(- q / 2 + sqrt(Q)) - cbrt(-q / 2 - sqrt(Q))
        y2 = complex(- 0.5 * y1, (sqrt(3) / 2) * y11)
        y3 = y2.conjugate()
        print(f'Корнями уравнения являются:\nx1= {y1 - xy}\nx2= {y2 - xy}\nx3= {y3 - xy}')
    elif Q == 0:
        y1 = 2 * cbrt(- q / 2)
        y2 = - cbrt(-q / 2)
        print(f'Корнями уравнения являются:\nx1= {y1 - xy}\nx2= {y2 - xy}')
    else:
        if q < 0:
            fi = atan(sqrt(-Q) / (-q / 2))
            m = cub_eq_3(fi, p)
        elif q > 0:
            fi = atan(sqrt(-Q) / (-q / 2)) + pi
            m = cub_eq_3(fi, p)
        else:
            fi = pi / 2
            m = cub_eq_3(fi, p)
        print(f'Корнями уравнения являются:\nx1= {m[0] - xy}\nx2= {m[1] - xy}\nx3= {m[2] - xy}')


# Calculation of the quadratic equation.
def quadratic_equation(a, b, c):
    disc = b**2 - 4 * a * c
    if disc > 0:
        x1 = ((-b) + sqrt(disc)) / (2 * a)
        x2 = ((-b) - sqrt(disc)) / (2 * a)
        print(f"Уравнение имеет 2 корня:\nx1= {x1}\nx2= {x2}")
    elif disc == 0:
        x = (-b) / (2 * a)
        print(f"Уравнение имеет корень\n:x1= {x}")
    else:
        print('Уравнение не имеет корней')


# Checking for float.
def dig_val(x, s=''):
    while True:
        try:
            return float(x)
            break
        except ValueError:
            x = input(f'Введено не число. Попробуйте снова. {s}\n')


# Manual input for equations.
def manual_inp(eq, allk, pa):
    if allk != []:
        question = eq[len(allk[0]):]
        allk = re.findall(pa, question)
        task.append(allk)
        return [allk, question]
    else:
        allk = re.findall(pa, eq)
        task.append(allk)
        return [allk, eq]


pat = [r'[^a-zA-z]*x\^3', r'[^a-zA-z]*x\^2', r'[^a-zA-z]*x', r'[^a-zA-z]+=0']
patt = ['x^3', 'x^2', 'x', '=0']
task = []
allk = []


question = input('День добрый. Вводить уравнение по элементам или целиком? (Введите номер варианта 1/2):\n')
if question == '1':
    question = input('У вас кубическое или квадртаное уравнение? (Введите номер варианта 1/2):\n')
    while True:

        if question == '1':
            a, b, c, d = [dig_val(input(f'Введите значение перед {i}:\n')) for i in patt]
            cubic_equation(a, b, c, d)
            break

        elif question == '2':
            a, b, c = [dig_val(input(f'Введите значение перед {i}:\n')) for i in patt[1:]]
            quadratic_equation(a, b, c)
            break
        else:
            question = int(input('Введено неверное число. Попробуйте снова! '
                                 '(Введите номер варианта 1/2):\n'))

elif question == '2':
    question = input('Введите уравнение типа 2x^2+3x-5=0:\n')

    for i in range(len(pat)):
        vop = manual_inp(question, allk, pat[i])
        question, allk = vop[1], vop[0]
        try:
            task[i] = task[i][0].replace(patt[i], '')
        except IndexError:
            task[i] = ''
        if task[i] == '':
            task[i] = '0'
        elif task[i] == '-':
            task[i] = '-1'
        elif task[i] == '+':
            task[i] = '1'

    if task[0] != '0':
        cubic_equation(float(task[0]), float(task[1]), float(task[2]), float(task[3]))
    elif task[0] == '0':
        quadratic_equation(float(task[1]), float(task[2]), float(task[3]))
else:
    question = int(input('Введено неверное число. Попробуйте снова! (Введите номер варианта 1/2):\n'))
