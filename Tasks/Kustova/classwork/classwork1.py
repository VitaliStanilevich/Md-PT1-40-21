numbers = {'one':1, 'two':2,'three':3,'four':4, 'five':5, 'six':6,'seven':7,
 'eight':8, 'nine': 9, 'ten':10, 'eleven':11, 'twelve':12, 'thirteen':13, 'fourteen':14,
 'fifteen':15, 'sixteen':16, 'seventeen':17, 'eighteen':18, 'nineteen':19, 'twenty':20}

list = input('enter your string:\n').split(' ')    
list_numb = []
for i in list:                                    #преобразование списка в числа, исключение дубликатов
    if numbers[i] not in list_numb:
        list_numb.append(numbers[i])
sort_list = sorted(list_numb)                    #сортировка по возрастанию
print(sort_list)
sum_odd = 0  
for i in range(len(sort_list) - 1):                  # произведение первого и второго, сумма второго и третьего и т.д. + сумма нечетных
    if i%2 == 1:
        sum_odd += i
    if i%2 == 0:
        print(sort_list[i]*sort_list[i+1], end = ', ')
    else:
        print(sort_list[i]+sort_list[i+1], end = ', ')
print('cумма всех нечетных =', sum_odd)                                          


