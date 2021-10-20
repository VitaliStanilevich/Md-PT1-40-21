"""
Кубическое уравнение в общем виде:
ax^3 + bx^2 + cx + d = 0

Кубическое уравнение в каноническом виде:
y^3 + py + q = 0

Замена переменной и коэффициенты:
x = y - b/3a
p = c/a - b^2/3a^2
q = 2b^3/27a^3 - bc/3a^2 + d/a

Формула Кардано:
Q = (p/3)^3 + (q/2)^2
alpha = (-q/2 + Q^(1/2))^(1/3)
beta = (-q/2 - Q^(1/2))^(1/3)

Q > 0: 1 вещественный + 2 комплексных корня
y1 = alpha + beta
y2 = -(alpha + beta)/2 + i(alpha - beta)/2 * 3^(1/2)
y3 = -(alpha + beta)/2 - i(alpha - beta)/2 * 3^(1/2)

Q = 0: 1 вещественный + 2 вещественных корня
alpha = beta
y1 = 2alpha
y2 = -alpha
y3 = -alpha

Q < 0: 3 вещественных корня
y1 = 2(-p/3)^(1/2) * cos(arccos(3q/2p(-3/p)^(1/2))/3 - 2*pi*0/3)
y2 = 2(-p/3)^(1/2) * cos(arccos(3q/2p(-3/p)^(1/2))/3 - 2*pi*1/3)
y3 = 2(-p/3)^(1/2) * cos(arccos(3q/2p(-3/p)^(1/2))/3 - 2*pi*2/3)
"""

from math import cos, acos, pi


def check(a, b, c, d, x):
    return round(abs(a*x**3 + b*x**2 + c*x + d), 6)


print("Введите коэффициенты уравнения:")
a, b, c, d = float(input()), float(input()), float(input()), float(input())
# a, b, c, d = 1, 3, 0, 1     # Q>0
# a, b, c, d = 1, 3, 0, -1    # Q<0
# a, b, c, d = 1, 3, 0, 0     # Q=0, p!=0, q!=0
# a, b, c, d = 1, 3, 3, 1     # Q=0, p==0, q==0

p = c/a - (b**2)/(3*a**2)
q = (2*b**3)/(27*a**3) - (b*c)/(3*a**2) + d/a
Q = (p/3)**3 + (q/2)**2
# print("p =", p)
# print("q =", q)
# print("Q =", Q)

if Q > 0:
    alpha_exp = -q/2 + Q**(1/2)
    beta_exp = -q/2 - Q**(1/2)
    alpha = alpha_exp**(1/3) if alpha_exp > 0 else -(-alpha_exp)**(1/3)
    beta = beta_exp**(1/3) if beta_exp > 0 else -(-beta_exp)**(1/3)

    # 1 вещественный, 2 комплексных
    y1 = alpha + beta
    y2 = complex(-(alpha + beta)/2, +(alpha - beta) * 3**(1/2)/2)
    y3 = complex(-(alpha + beta)/2, -(alpha - beta) * 3**(1/2)/2)
elif Q == 0:
    # alpha = beta
    alpha = (-q/2)**(1/3) if -q/2 > 0 else -(q/2)**(1/3)
    # 3 вещественных
    y1 = 2*alpha
    y2 = -alpha
    y3 = -alpha
else:
    # 3 вещественных
    k = 2 * (-p/3)**(1/2)
    arg = acos(3*q/(2*p) * (-3/p)**(1/2)) / 3
    y1 = k * cos(arg)
    y2 = k * cos(arg - 2*pi/3)
    y3 = k * cos(arg - 4*pi/3)

x1 = y1 - b/(3*a)
x2 = y2 - b/(3*a)
x3 = y3 - b/(3*a)

print("x1 =", x1)
print("x2 =", x2)
print("x3 =", x3)

# print("Check x1:", check(a, b, c, d, x1))
# print("Check x2:", check(a, b, c, d, x2))
# print("Check x3:", check(a, b, c, d, x3))
