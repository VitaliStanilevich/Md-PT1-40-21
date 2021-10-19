from locale import setlocale,LC_ALL
from datetime import datetime
from num2t4ru import num2text 
from pymorphy2 import MorphAnalyzer
 
morph = MorphAnalyzer()
 
 
def make_dates(declinatio=None):
    if declinatio is None:
        # имя прилагательное, порядковое, средний род, единственное число, номинатив
        declinatio = {'ADJF','Anum','neut','sing','nomn'}
    
    NUMR = {}
    
    for i in range(1,32):    
        text = num2text(i) # преобразуем числа в числительные
        text_ = text.split()
        # склоняем
        word1 = morph.parse(text_[-1])[0].inflect(declinatio).word
        if len(text_) == 1:
            NUMR[i] = word1
        else:
            NUMR[i] = text_[0] + ' ' + word1
    return NUMR
 
def make_year(year,declinatio=None):
    # имя прилагательное, порядковое, средний род, единственное число, род. падеж
    if declinatio is None:
        declinatio = {'ADJF','Anum','neut','sing','gent'}
    
    text = num2text(int(year)) # преобразуем числа в числительные
    text_ = text.split()
    
    # склоняем
    word1 = morph.parse(text_[-1])[-1].inflect(declinatio).word 
    if len(text_) == 1:
        year = word1
    else:
        year  = ' '.join(text_[:-1] + [word])
    return year
 
 
if __name__ == '__main__':   
 
    dates = make_dates() # получаем словарь дат вида 
    # {'1':'первое','2':'второе',... '10':'десятое','11':'одинадцатое',... '31':'тридцать первое'}
    print(dates)
    
    dt = input('Введите дату в формате день.месяц.четыре_цифры_года:')
    #dt = '31.12.2017'
    # парсим дату
    dt = datetime.strptime(dt, "%d.%m.%Y")
    print(dt)
    setlocale(LC_ALL, "") # включаем локализацию
    # форматируем
    str_dt = dt.strftime("%d %B %Y")
    print(str_dt) # локализованная дата
    date, month, year = str_dt.split() # разбиваем на составляющие
    date = dates[int(date)] # извлекаем дату в виде порядкового числительного
    # приводим месяц к нужной форме существительного в родительном падеже
    month = morph.parse(month)[0].inflect({'NOUN','sing','gent'}).word
    
    str_dt = '{date} {month} {year} года'.format(
        date=date.capitalize(),
        month=month,
        year=year)
    
    print(str_dt) 
    # Тридцать первое декабря 2017 года
    
    str_dt = '{date} {month} {year} года'.format(
        date=date.capitalize(),
        month=month,
        year=make_year(year))
    
    print(str_dt) 
    # Тридцать первое декабря две тысячи семнадцатого года