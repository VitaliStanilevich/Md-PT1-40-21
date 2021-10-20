
import datetime 

dt_now = str(datetime.datetime.now())
f1=dt_now.split(":")
min=f1[1]
f2=f1[0].split(" ")
hour=f2[1]
time=hour+":"+min
print("Текущее время:", time, end="\n")

in_time=input("введите значение времени в виде hh:mm: ")
s_time=in_time.split(":")
hours=s_time[0]
min=s_time[1]

h_dict = { 1: "первого ", 2: "второго",3: "третьего",4: "четвертого",5: "пятого",6: "шестого",                  #словарь часов
7: "седьмого", 8: "восьмого", 9: "девятого", 10: "десятого", 11: "одиннадцатого", 12: "двенадцатого"}

n=13
while int(n)<25:                  #расширение словаря часов
    h_dict[n]=h_dict[n-12] 
    n+=1

m_dict = { 1: " одна", 2: " две",3: " три",4: " четыре",5:" пять",6:" шесть",7: " семь",8: " восемь",9: " девять",  #словарь минут
10: " десять", 11: " одиннадцать",12: " двенадцать",13: " тринадцать",14: "четырнадцать",15: " пятнадцать",
16: " шестнадцать",17: "семнадцать",18: " восемнадцать",19: " девятнадцать",20: " двадцать", 30: " тридцать",
40: " сорок", 50: " пятьдесят"}

m=1
k=2
while int(m)<10 and k<5:                                  #расширение словаря минут  
        m_dict[m+k*10]=m_dict[k*10]+m_dict[m]
        m+=1
        if m==9:
            k+=1
            m=1


h_text=h_dict.get(int(hours))                        
m_text=m_dict.get(int(min)) 
h1_text=h_dict.get(int(hours)+1) 
m1_text=m_dict.get(60-int(min))

if int(min)<30:
    print (m_text+" минут "+h1_text)
elif int(min)==30:
    print ("половина "+h1_text)
elif int(min)>30 and int(min)<45:
    print (m_text+" минут ",h1_text)
elif int(min)>=45:
    print ("без "+m1_text+" минут "+h1_text)



