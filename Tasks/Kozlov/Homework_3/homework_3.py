import datetime

minutes_1 = ['одна', 'две', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять', 'одинадцать',
             'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать',
             'девятнадцать']
minutes_2 = ['двадцать', 'тридцать', 'сорок', 'пятьдесят']
minutes_3 = ['одной', 'двух', 'трех', 'четырех', 'восьми']
hours_1 = ['первого', 'второго', 'третьего', 'четвертого', 'пятого', 'шестого', 'седьмого', 'восьмого', 'девятого',
           'десятого', 'одинадцатого', 'двенадцатого']
hours_2 = ['час', 'два']
hours_ending = ['час', 'часа', 'часов']
minutes_ending = ['минута', 'минуты', 'минут']


# Formation of correct endings
def ham(x, m):
    if x % 10 == 1 and x != 11:
        return m[0]
    elif x % 10 in range(2, 5) and x not in range(12, 15):
        return m[1]
    else:
        return m[2]


# Start of the program.
question = input('День добрый. Желаете узнать время на данный момент или ввести свое? (Введите 1 или 2):\n')
while True:
    if question == '1':
        p_time = list(map(int, datetime.datetime.now().strftime("%H %M").split(' ')))
        break
    elif question == '2':
        p_time = input('Введите время в формате 10:23:\n')
        while True:
            try:
                p_time = list(map(int, p_time.split(':')))
                if len(p_time) == 2 and p_time[0] < 24 and p_time[1] < 60:
                    break
                else:
                    p_time = input('Некорректный ввод! Введите время в формате 10:23:\n')
            except:
                p_time = input('Некорректный ввод! Введите время в формате 10:23:\n')
        break
    else:
        question = input('Некорректный вариант выбора. Желаете узнать время на данный момент или ввести свое? '
                         '(Введите 1 или 2):\n')

# Transfer to 12 from 24 hours.
p_time[0] = p_time[0] - 12 if p_time[0] > 11 else p_time[0]
print('Время:')

# Conditions for the formation of text time.
if p_time[1] == 0:
    print(
        f'{f"{hours_2[1]} " if p_time[0] == 2 else f"{minutes_1[:12][p_time[0] - 1]} " if p_time[0] in [0, range(3, 13)] else ""}{ham(p_time[0], hours_ending)}.')
elif p_time[1] < 20:
    print(f'{minutes_1[p_time[1] - 1]} {ham(p_time[1], minutes_ending)} {hours_1[p_time[0]]}.')
elif p_time[1] in range(20, 30) or p_time[1] in range(31, 45):
    print(
        f'{minutes_2[p_time[1] // 10 - 2]}{f" {minutes_1[p_time[1] % 10 - 1]}" if p_time[1] % 10 != 0 else ""} {ham(p_time[1], minutes_ending)} {hours_1[p_time[0]]}.')
elif p_time[1] in range(45, 60):
    print(
        f'без {minutes_3[59 - p_time[1]] if 59 - p_time[1] in range(0, 4) else "восьми" if 60 - p_time[1] == 8 else minutes_1[59 - p_time[1]][:-1] + "и"} '
        f'{minutes_ending[1] if 59 - p_time[1] == 0 else minutes_ending[2]} {hours_2[p_time[0]] if p_time[0] in [0, 1] else minutes_1[p_time[0]]}.')
else:
    print(f'половина {hours_1[p_time[0]]}.')
