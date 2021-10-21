
l="five thirteen two eleven seventeen two one thirteen ten four eight five nineteen"

t_dict = { "zero": 0, "one": 1,"two": 2, "three":3, "four": 4, "five": 5,"six": 6,
"seven":7, "eight": 8, "nine": 9, "ten": 10, "eleven" :11, "twelve":12, "thirteen":13,
"fourteen": 14, "fifteen": 15, "sixteen":16, "seventeen":17, "eighteen":18, "nineteen":19,"twenty":20}

L=l.split(" ")
print(L)

for i in range(len(L)):                
    if L[i] in t_dict:                                 #1 задание
        L[i]=t_dict.get(L[i])
print ("Преобразование в числа:", L)


print ("Исключение дубликатов:", list(set(L)))         #2 задание

for i in range(len(L)):
    for j in range(i+1,len(L)):                      
        if L[i]>L[j]:                                  #3 задание
            L[i],L[j] = L[j],L[i]
print ("Сортировка:", L)

#L.sort()
#print("Сортировка:", L)

for i in range(0,len(L)-1,2):
        print("Произведение:",L[i]*L[i+1])             #4 задание
        print("Сумма:", L[i+1]+L[i+2])

k=0
while k<(len(L)-1):                                    #5 задание 
    if int(L[k])%2==0:
        del L[k]
        k-=1
    else:
       k+=1
print("Сумма всех нечетных чисел составляет:", sum(L))

       

                






