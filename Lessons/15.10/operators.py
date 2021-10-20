
for i in range(10):
    if i == 2 or i == 4:
        continue
    if i == 7:
        break
    print(i)
else:
    print("hello from else")