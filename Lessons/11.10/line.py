eq = input("Enter your eq:\n")
x = int(input("Enter the x:\n"))

# y=-3x+10
eq_short = eq.split('=')
print(eq_short)

coeff = eq_short[1].split('x')
k = 1 if coeff[0] == '' else -1 if coeff[0] == '-' else int(coeff[0])
b = int(coeff[1])

y = k*x + b
print(y)
# print(f"{1 if coeff[0] == '' else -1 if coeff[0] == '-' else int(coeff[0])*x + int(coeff[1])}")
