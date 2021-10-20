#строка числительных
dict = {1:"one",
        2:"two",
        3:"three",
        4:"four",
        5:"five",
        6:"six",
        7:"seven",
        8:"eight",
        9:"nine",
        10:"ten",
        11:"eleven",
        12:"twelve",
        13:"thirteen",
        14:"fourteen",
        15:"fifteen",
        16:"sixteen",
        17:"seventeen",
        18:"eighteen",
        19:"nineteen",
        20:"twenty"
       }

l = input("Введите строку, содержащую числительные больше 0 и меньше 21 через пробел:").split(" ")
print(f"Строка, преобразованная в коллекцию:\n{l}")
for i in range(len(l)):
    for k,v in dict.items():
        if l[i] == v:
            l[i] = k     
print(f"Строка, преобразованная в числа:\n{l}")
print(f"Строка без дубликатов:\n{set(l)}")
l=sorted(list(set(l)))
print(f"Отсортировать по возрастанию:\n{l}")
print("Последовательность сумма-произведение:")
for i in range(len(l)-1):
    print(l[i]*l[i+1]) if (i+1)%2 == 0 else print(l[i]+l[i+1])
sum = 0    
for i in l:
    if i%2 != 0:
        sum = sum + i 
print(f"Сумма нечетных чисел:{sum}")


   