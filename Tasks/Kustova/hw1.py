start_sum = 20000
time = 0
percent = 15
while time != 60:
    start_sum = start_sum + (start_sum * percent/100)/12
    time+=1
print("Депозит со стартовой суммой 20000 через 5 лет выльется в", round(start_sum,1))