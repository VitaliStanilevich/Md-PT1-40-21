from num2t4ru import num2text
import pymorphy2 
def get_number_and_noun(numeral, noun): 
    morph = pymorphy2.MorphAnalyzer() 
    word = morph.parse(noun) 
    v1, v2, v3 = word.inflect({"sing", "nomn"}), word.inflect({"gent"}), word.inflect({"plur", "gent"}) 
    return num2text(num=numeral, main_units=((v1.word, v2.word, v3.word), "m")) 
result = get_number_and_noun(123452, "доллар")
print(result)