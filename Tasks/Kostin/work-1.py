
import math
print("введите данные для уранения вида y=kx-d")

k=int(input())
d=int(input())

if d < 0:
    zin = "+"
    d=d*-1
else:
    zin = "-"

const1="введите данные для x уранения вида y={}x{}{}"



print(const1.format(k,zin,d))

x=int(input())

y=k*x-d

print("итог",y)


