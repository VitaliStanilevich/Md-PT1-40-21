import re


def quadratic_equation(a, b, c):
    disc = (b**2 - 4 * a * c)**0.5
    if disc > 0 :
        x1 = ((-b) + disc) / (2 * a)
        x2 = ((-b) - disc) / (2 * a)
        print(f"Уравнение имеет 2 корня: {x1} и {x2}")
    elif disc == 0:
        x = (-b) / (2 * a)
        print(f"Уравнение имеет корень {x}")
    else:
        print('Уравнение не имеет корней')

question = int(input('День добрый. Будем вводить уравнение целиком (пример: 2x^2+3x-5=0) или отдельными числами? '
                 '(Введите номер варианта 1/2):\n'))
while True:
    if question == '2':
        a, b, c = int(input('Введите значение перед x^2:\n')), int(input('Введите значение перед x:\n')), \
                  int(input('Введите последнее значение:\n'))
        quadratic_equation(a, b, c)
        break
    elif question == 1:
        eq = re.sub('x\^2', ',', input('Введите уравнение:\n'))
        eq = re.sub('x', ',', eq)
        eq = re.sub('=0', '', eq)
        eq = eq.split(',')
        print(eq)
        quadratic_equation(int(eq[0]), int(eq[1]), int(eq[2]))
        break
    else:
        question = int(input('Введено неверное число. Попробуйте снова! '
                         '(Введите номер варианта 1/2):\n'))
