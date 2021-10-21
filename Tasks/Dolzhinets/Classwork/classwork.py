test_str = "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen"

numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 
'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 
'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 
'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 
'nineteen': 19, 'twenty': 20}
print([numbers[i] for i in test_str.split(" ")]) #преобразуем в числа 
print(set([numbers[i] for i in test_str.split(" ")])) #исключаем дубликаты
sort_list = sorted(set([numbers[i] for i in test_str.split(" ")])) #методом sorted  сортируем set и получаем отсортированный список

#сумма нечётных чисел списка
count = 0
for i in sort_list:
    if i % 2 == 1:
        count += i
print(count)

#произведение первого и второго, сумма второго и третьего и так далее
new_l1 = []  #создаем список куда будем добавлять полученные значения
for i in range(len(sort_list) - 1): #цикл 
    if  i %2 == 0: #если индекс в списке четный, то 
        fin = sort_list[i] * sort_list[i + 1] #находим произведение индекса и следующего за ним
        new_l1.append(fin) #добавляем полученное значение в список
    elif i %2 != 0: #если индекс нечетный, то
        fin2 = sort_list[i] + sort_list[i + 1] #складываем индекс и последующий элемент
        new_l1.append(fin2) #добавляем полученное значение в список
print(new_l1)