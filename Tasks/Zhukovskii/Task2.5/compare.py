s1 = input('Введите строку 1: ')
s2 = input('Введите строку 2: ')
l = len(s1)
q = 0
z = 0
i = 0
a = l-1
b = 0
x = 0
w = 0
if len(s1)==len(s2):
    while q < l:
        if ord(s1[q]) == ord(s2[q]):
            z +=0 
            q +=1
        else:
            z = 1
            break
    if z == 0:
        print("Строки равны")
    else:
        print("Строки не равны")
    print("Строка 2 не является подстрокой")
elif len(s1) > len(s2):
    i = s1.find(s2)
    p = i+len(s2)
    while i < p:
        if ord(s1[i])==ord(s2[q]):
            w +=0
            i +=1
            q +=1
        else:
            w = 1
            break
    if w == 0:
        print("Строка 2 является подстрокой")
        print("Строки не равны")
    else:
        print("Строка 2 не является подстрокой")
        print("Строки не равны")
else: 
    print("Строки не равны")
while b <= a:
        if ord(s1[b])==ord(s1[a]):
            x +=0 
            a -=1
            b +=1
        else:
            x = 1
            break
if x == 0:
    print("Строка 1 полидром")
else:
    print("Строка 1 не полидром")