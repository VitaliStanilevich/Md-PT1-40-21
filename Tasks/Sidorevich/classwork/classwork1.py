lst = input("Enter a string:\n").split(' ')

numbers = {'one': 1,
           'two': 2,
           'three': 3,
           'four': 4,
           'five': 5,
           'six': 6,
           'seven': 7,
           'eight': 8,
           'nine': 9,
           'ten': 10,
           'eleven': 11,
           'twelve': 12,
           'thirteen': 13,
           'fourteen': 14,
           'fifteen': 15,
           'sixteen': 16,
           'seventeen': 17,
           'eighteen': 18,
           'nineteen': 19,
           'twenty': 20
           }

# Преобразовать в числа
for i in range(len(lst)):
    lst[i] = numbers.get(lst[i])

print(lst)

# Исключить дубликаты & по возрастанию
print(list(set(lst)))

# Произведение, сумма
for i in range(len(lst)-1):
    print(lst[i] * lst[i+1] if i % 2 == 0 else lst[i] + lst[i+1], end=' ')

# print([lst[2*i] * lst[2*i+1] for i in range(len(lst)//2)])
# print([lst[2*i+1] + lst[2*i+2] for i in range(len(lst)//2 - 1)])

# Сумма нечетных
print(f"\nSum = {sum([lst[i] for i in range(len(lst)) if lst[i] % 2 != 0])}")
