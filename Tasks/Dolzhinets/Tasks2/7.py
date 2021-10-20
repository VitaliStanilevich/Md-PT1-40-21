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
input('text')
print()