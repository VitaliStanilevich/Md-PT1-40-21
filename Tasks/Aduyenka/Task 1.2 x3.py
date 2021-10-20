import numpy as np

 #ax^3+bx^2+cx+d=0 - типовая форма уравнения
 # y^3+p*y+q=0 Формула Кардана

a=int(input("ввведите значение a: "))
b=int(input("ввведите значение b: "))
c=int(input("ввведите значение c: "))
d=int(input("ввведите значение d: "))

p=float((3*a*c-np.sqrt(b)/(3*np.sqrt(a))))
print (p)
q=float(2*np.cbrt(b)-9*a*b*c+(27*(np.sqrt(a))*d)/(27*np.cbrt(a)))
print (q)
Q=float(np.cbrt(p/3)+np.sqrt(q/2))
print ("Q равно", Q )

alf=np.cbrt(-(q/2)+(np.sqrt(Q)))
betta=np.cbrt(-(q/2)-(np.sqrt(Q)))

print ("alf равно", alf )
print ("betta равно", betta )

y1=alf+betta
x1=y1-(b/(3*a))
y2=complex(-((alf+betta)/2)+((alf-betta)/2)*np.sqrt(3))
x2=y2-(b/(3*a))
y3=complex(-((alf+betta)/2)-((alf-betta)/2)*np.sqrt(3))
x3=y3-(b/(3*a))

if Q>0:
    print ("Уравнение имеет вещественный корень" , x1, end="\n")
    print ("Уравнение имеет сопряжённый комплексный корень" , x2 , end="\n")
    print ("Уравнение имеет сопряжённый комплексный корень" , x3 , end="")
elif Q==0:
    if p==q==0:
        print ("Уравнение имеет один трёхкратный вещественный корень" )
    else:
        print ("Уравнение имеет один однократный вещественный корень и один двукратный")
elif Q<0:
     print ("Уравнение имеет три вещественных корня")




