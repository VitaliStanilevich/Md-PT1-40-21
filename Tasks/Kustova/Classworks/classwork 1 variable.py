s = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty']

for i in input('enter your string:\n').split(' '):
    s.append(s.index(i) + 1 )
else:
    del s [:20]
                    
s = list(set(s))   
print(s)                                 # п.1-3 (преобразованы в числа, исключены дубликаты, отсортированы по возрастанию)

print('Произведение первого и второго, сумма третьего и четвертого и т.д: ', end = ' ')
s.append(0)
for i in range(len(s) - 1):   
    if s[i]%2 == 1:
        s[-1] += s[i]
        if i == (len(s) - 2):
            break
    if i%2 == 0:
        print(s[i]*s[i+1], end = ', ')
    else:
        print(s[i]+s[i+1], end = ', ')
print('cумма всех нечетных чисел =', s[-1] )     