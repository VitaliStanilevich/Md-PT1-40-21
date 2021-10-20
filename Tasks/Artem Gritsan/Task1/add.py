from re import search
x, y = input('Введите первую строку:\n'), input('Введите вторую строку:\n')
if len(x) == len(y):
    if x[0] == y[0]:
        i = 1
        while x[i] == y[i]:
            p = 'Строки равны'
            if i < len(x) - 1:
                i += 1
            else:
                break
        else:
            p = 'Строки не равны'
    else:
        p = 'Строки не равны'
else:
    p = 'Строки не равны'
    if x.lower().find(y.lower()) != -1:
        print('Вторая строка является подстрокой первой строки')
    else:
        print('Вторая строка не является подстрокой первой строки')
print(p)

if x.lower() == x[::-1].lower():
    print('Первая строка является палиндромом')
else:
    print('Первая строка не является палиндромом')
