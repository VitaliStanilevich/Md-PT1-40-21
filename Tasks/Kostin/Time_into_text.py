from datetime import datetime
#решаем какой ввод нужен
print("выберите вариант работы кода: 1 - ввести время; 2 - текущее время")

des=int(input())

#определяем часы-минуты
if des == 1:
    
    print("введите часы")
    h=int(input())
    print("введите минуты")
    m=int(input())

    if h>24 or m>60:
        print("Не прокатит, берём текущее время")
        a=datetime.now()
        h=a.hour
        m=a.minute
elif des==2: 

    a=datetime.now()
    h=a.hour
    m=a.minute
else:
    print("Шутники, берём текущее время")
    a=datetime.now()
    h=a.hour
    m=a.minute

#словари
d1=dict([(0,"ноль"),(1,"первого"),(2,"второго"),(3,"третьего"),(4,"четвёртого"),(6,"шестого"),(5,"пятого"),(7,"седьмого"),(8,"восьмого"),(9,"девятого"),(10,"десятого"),(11,"одинадцатого"),(12,"вдвенадцатого"),(13,"первого"),(14,"второго"),(15,"третьего"),(16,"четвёртого"),(18,"шестого"),(17,"пятого"),(19,"седьмого"),(20,"восьмого"),(21,"девятого"),(22,"десятого"),(23,"одинадцатого"),(24,"вдвенадцатого")])
d2=dict([(0,"ноль"),(1,"один"),(2,"два"),(3,"три"),(4,"четыре"),(5,"пять"),(6,"шесть"),(7,"семь"),(8,"восемь"),(9,"девять"),(10,"десять"),(11,"одиннадцать"),(12,"двенадцать"),(13,"тринадцать"),(14,"четырнадцать"),(15,"пятнадцать"),(16,"шестнадцать"),(17,"семнадцать"),(18,"восемнадцать"),(19,"девятнадцать"),(20,"двадцать"),(21,"двадцать одна"),(22,"двадцать две"),(23,"двадцать три"),(24,"двадцать четыре"),(25,"двадцать пять"),(26,"двадцать шесть"),(27,"двадцать семь"),(28,"двадцать восемь"),(29,"двадцать девять"),(30,"половина"),(31,"тридцать один"),(32,"тридцать два"),(33,"тридцать три"),(34,"тридцать четыре"),(35,"тридцать пять"),(36,"тридцать шесть"),(37,"тридцать семь"),(38,"тридцать восемь"),(39,"тридцать девять"),(40,"сорок"),(41,"сорок один"),(42,"сорок два"),(43,"сорок три"),(44,"сорок четыре"),(45,"сорок пять"),(46,"сорок шесть"),(47,"сорок семь"),(48,"сорок восемь"),(49,"сорок девять"),(50,"пятьдесят"),(51,"пятьдесят один"),(52,"пятьдесят два"),(53,"пятьдесят три"),(54,"пятьдесят четыре"),(55,"пятьдесят пять"),(56,"пятьдесят шесть"),(57,"пятьдесят семь"),(58,"пятьдесят восемь"),(59,"пятьдесят девять"),(60,"шестьдесят")])
d3=dict([(0,"ноль часов"),(1,"один час"),(2,"два часа"),(3,"три часа"),(4,"четыре часа"),(5,"пять часов"),(6,"шесть часов"),(7,"семь часов"),(8,"восемь часов"),(9,"девять часов"),(10,"десять часов"),(11,"одиннадцать часов"),(12,"двенадцать часов"),(13,"один час"),(14,"два часа"),(15,"три часа"),(16,"четыре часа"),(17,"пять часов"),(18,"шесть часов"),(19,"семь часов"),(20,"восемь часов"),(21,"девять часов"),(22,"десять часов"),(23,"одиннадцать часов"),(24,"двенадцать часов")])
d4=dict([(1,"минут"),(2,"минуты"),(3,"минута"),(4,"")])
d5=dict([(1,"часа"),(2,"час"),(3,"часов"),(4,"")])
d6=dict([(1,"одной"),(2,"двух"),(3,"трёх"),(4,"четырех"),(5,"пяти"),(6,"шести"),(7,"семи"),(8,"восьми"),(9,"девяти"),(10,"десяти"),(11,"одиннадцати"),(12,"двенадцати"),(13,"тринадцати"),(14,"четырнадцати")])
d7=dict([(1,"час"),(2,"два"),(3,"три"),(4,"четыре"),(5,"пять"),(6,"шесть"),(7,"семь"),(8,"восемь"),(9,"девять"),(10,"десять"),(11,"одиннадцать"),(12,"двенадцать"),(13,"час"),(14,"два"),(15,"три"),(16,"четыре"),(17,"пять"),(18,"шесть"),(19,"семь"),(20,"восемь"),(21,"девять"),(22,"десять"),(23,"одиннадцать"),(24,"двенадцать")])
d8=dict([(1,"одна"),(2,"две"),(3,"три"),(4,"четыре")])

#вилка часов
var3=[1]
var4=[2,3,4]
if h in var3:
    hc=2 
elif h in var4:
    hc=1 
else:
    hc=3

h2=h+1

#вилка минут
var1=[1,21]# минута
var2=[2,3,4,22,23,24]# минуты
var5=[30]#половина
var6=[0]
if m in var1:
    mc=3 
elif m in var2:
    mc=2
elif m in var5:
    mc=4
elif m in var6:
    mc=4  
else:
    mc=1

#выборка значений из словарей
dh=d1[h]
dm=d2[m]
dmc=d4[mc]
dhc=d5[hc]
dhcr=d3[h]

#вилка формата
var_cor=[1,2,3,4]
if 0<m<30 and m in var_cor:
    dm=d8[m]
    dh=d1[h2]
    print(dm,dmc,dh) 
elif 0<m<30:
    dh=d1[h2]
    print(dm,dmc,dh)  
elif m==30:
    dh=d1[h2]
    print(dm,dh)#половина первого
elif 30<m<=45:
    dh=d1[h2]
    print(dm,dmc,dh)
elif m>45:
    dh=d1[h2]
    m=60-m
    dm=d6[m]   
    print("без",dm,dmc,dh)
elif m==0:
    print(dhcr,"ровно")  
