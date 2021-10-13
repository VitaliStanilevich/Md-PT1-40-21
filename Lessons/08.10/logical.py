num = 10

if num > 0:
    print("positive")
elif num == 0:
    print("zero")  
# if num == 0:
#     print("zero")
else:
    print("negative")

print("positive") if num > 0 else print("zero") if num == 0 else print("negative")



if num >= 0:
    if num == 0:
        print("zero")
    else:
        print("positive")
else:
    print("negative")

print("zero") if num == 0 else print("positive") if num >= 0 else print("negative")

# x = 10 if num >= 0 else -10

# if num >= 0:
#     x = 10
# else:
#     x = -10