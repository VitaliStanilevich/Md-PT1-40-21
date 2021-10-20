# #Пользователь вводит две строки - str1 и str2
# 1. Проверить, равны ли данные строки (str1 == str2 запрещено)
# 2. Проверить, является ли str2 подстрокой str1 (str2 in str1 запрещено)
# 3. Проверить, является ли str1 палиндромом
def get_string():
    while True:
        user_string = str(input())
        if user_string:
            break
    return user_string

def compare_strings(s1,s2):
    if s1.find(s2) == s2.rfind(s1) and s1.find(s2) != -1:
        print("\nThe strings are the same.")
    else:
        print("\nThe strings are different.")

def substring(s1,s2):
    if s1.find(s2) == -1:
        print("The second string is not included in the first string.")
    else:
        print("The second string is included in the first string.")

def palindrome1(s):
    # Палиндром  — число, буквосочетание, слово или текст, одинаково читающееся в обоих направлениях.
    l=[]
    for i in s:
        if i.isalpha() or i.isdigit():
           l.append(i)
    if len(l) == 0:
        print("There aren't a word, number, phrase, or other sequence of characters which reads.")
    elif len(l)%2 == 0:
        if l[0:len(l)//2:1] == l[len(l)-1:len(l)//2-1:-1]:
            print("The string is palindrome.")
        else:
            print("The string isn't palindrome.")
    else:
        if l[0:len(l)//2:1] == l[len(l)-1:len(l)//2:-1]:
            print("The string is palindrome.")
        else:
            print("The string isn't palindrome.")

def palindrome2(s):
    # Палиндром  — любой симметричный относительно своей середины набор символов.
    if len(s)%2 == 0:
        if s[0:len(s)//2:1] == s[len(s)-1:len(s)//2-1:-1]:
            print("The string is a character set symmetrical about its middle.")
        else:
            print("The string isn't a character set symmetrical about its middle.")
    else:
        if s[0:len(s)//2:1] == s[len(s)-1:len(s)//2:-1]:
            print("The string is a character set symmetrical about its middle.")
        else:
            print("The string isn't a character set symmetrical about its middle.")

print("Enter the first string:")
str1 = get_string()
print("Enter the second string:")
str2 = get_string()
compare_strings(str1,str2)
substring(str1,str2)
print("\nThis is information about the first string:")
palindrome1(str1)
palindrome2(str1)



 