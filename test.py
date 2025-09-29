""" Мова Python має наступний перелік зарезервованих слів: False, None,
True, and, as, assert, async, await, break, class, continue, 
def, del, elif, else, except, finally, for, from, global, 
if, import, in, is, lambda, nonlocal, not, or, pass, raise, 
return, try, while, with, yield. Ми вивчимо ці оператори протягом курсу
але запам'ятай, що використовувати їх як ім'я для змінної не можна. """


""" user_name = input("name ")
age = input("Age  ")

print(user_name, age )
 """

"""  age = 16
namber = 19
nb = age >= namber
print(nb)

age = 16
namber = 19
nb = age == namber
print(nb)


age = 16
namber = 19
nb = age != namber
print(nb)


age = 16
namber = 19
nb = age <= namber
print(nb)
 """

""" import time
love = ("i love you")

delay = 0.3 # Затримка в секундах

for i in range(len(love)):
    print(love[i], end='', flush=True)
    time.sleep(delay)
print() # Для переходу на новий рядок після завершення виведення """

""" index = ("hero")
print(index[0], index[1], index[2], index[3]) """

""" mein_name = input("Введи своє ім’я: ")
mein_age = int(input("Введи свій вік:"))
wird = ("Через 5 років")

age_5 = mein_age + 5

print(f"Привіт, {mein_name}! Тобі {mein_age} років.")
print(f"{wird} тобі буде {age_5}.") """

""" import random
kosten = random.randint(30, 2000)
produkten = int(input("Скількі ви хочете товарів: "))

produkten_kosten = produkten * kosten

print(f"Ти купив {produkten} товар(и) по {kosten}грн. Загальна сума: {produkten_kosten} грн.") """

""" schuger = int(input("скільки всього цукерок у коробці: ")) #Коли обчислюю дві дії то потрібно 
kids_schuger = int(input("скільки дітей отримають цукерки: "))#використовувати int і даже коли щось одне використовую 

frik_schger = schuger // kids_schuger
frik_msik = schuger % kids_schuger #для вичеслення залишку 

print(f"У кожної дитини буде по {frik_schger} цукерки. Залишок цукерок: {frik_msik}") """