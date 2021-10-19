s = "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen"
d = {"five": 5, "thirteen": 13, "two": 2, "eleven": 11, "seventeen": 17, "one": 1, "ten": 10, "four": 4, "eight": 8, "nineteen": 19}

#преобразовать в числа
l = [d[el] for el in s.split()]
print(l)

#отсортировать по возрастанию
order_l = sorted(l)
print(order_l)

#исключить дубликаты
new_l = list(set(l))
print(new_l)

#вывести полную сумму всех нечётных чисел
x = 0
for i in range(len(new_l)):
    if new_l[i] % 2 == 1:
        x += new_l[i]
print(x)