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



""" some_iterable = ["a", "b", "c"]
first_letter = some_iterable[-0]
middle_one = some_iterable[-1]
last_letter = some_iterable[-2]

print(first_letter, middle_one, last_letter)

some_iterable = [1, 2, 3, 4]
some_iterable[1] = 22222
print(some_iterable) """

""" chars = ['a', 'b', 'c']

list = chars.pop(1)
print(list)

 """

""" chars = ['a', 'b', 'c']
numbers = [1, 2]
chars.extend(numbers)
print(chars) """

""" age = 52
age *= 7 # скорочення
print(age)  """

""" test_age = int(input("твій вік: "))

if test_age >= 18:
    print("ти можеш проводити час як хочеш")
elif test_age >= 16:
    print("2 години")
else:
   print("ти не можеш проводити час як хочеш") """

# ТЗ:
# Напиши програму, яка запитує число у користувача
# і виводить "Парне", якщо воно парне, і "Непарне", якщо ні.

""" user_nambers = int(input("your numbers: ")) #Умова парності: Число є парним, 
if user_nambers  % 2 == 0:
    print("парне")     #якщо при діленні на 2 воно не залишає остачі, тобто остача дорівнює 0
else: 
    print("Непарне") """

# ТЗ:
# Користувач вводить число.
# Програма визначає: це позитивне, негативне чи нуль.
""" 
user_tex = int(input("your numbers: "))
if user_tex  == 0:
    print("нуль")
elif user_tex >= 0: 
    print("positiv")
else:
    print("negativ") """

# ТЗ:
# Програма запитує пароль.
# Якщо введено "python123", виводить "Доступ дозволено".
# Інакше — "Неправильний пароль".

""" passwort = input("passwort: ")

if passwort == "python123":
 print("Доступ дозволено")
else:
 print("Неправильний пароль")
 """
""" passwort = input("passwort: ") """

""" if passwort == "python123":
    print("Доступ дозволено")
else:
    print("Неправильний пароль") """


# kontrol l putzt alle in terminan

# ТЗ:
# Запитай температуру (у градусах Цельсія).
# Якщо менше 0 — виведи "Мороз".
# Якщо від 0 до 20 — "Прохолодно".
# Якщо більше 20 — "Тепло".

""" user_temperatur = int(input("градуси: "))

if user_temperatur < 0:
    print("Мороз")
elif user_temperatur <= 20:
    print("Прохолодно")
elif user_temperatur > 35:
    print(" жара")# print має бути на рівні з іншими типу пробілу
else:
    print("Тепло") """

# ТЗ:
# Користувач вводить оцінку (0-100).
# Виведи:
# 90-100 -> "Відмінно"
# 70-89  -> "Добре"
# 50-69  -> "Задовільно"
# менше 50 -> "Погано"

""" user = int(input("оціни роботу від (0 - 100): "))

if user >= 90:
    print("Відмінно")
elif user >= 70:
    print("Добре")
elif user >= 50:
    print("Задовільно")
else:
    print("Погано") #ураааа з першого разу написав

 """
""" 
x = int(input('Введіть число: '))

if x % 2 == 0:
    print("Число x є парним.")
else:
    print("Число x є непарним.")
 """

""" name_user = [1, 2, 3, 4, 5]
user = name_user
name = [1, 2, 3, 4, 5]
if user is name_user:
    print("правда")
else:
    print("неправда") 
  """

# Написати програму, яка приймає список чисел від користувача,
#  сортує їх від найменшого до найбільшого і виводить результат.

# 📋 Умови:
# Користувач вводить кілька чисел через пробіл.
# Програма перетворює ці числа у список.
# Сортує список у порядку зростання (від найменшого до найбільшого).
# Виводить відсортований список на екран.
""" """ 
""" def nambers_sort(nambers):
    nambers.sort()
    print('Відсортовані числа: ', nambers)

user = input('nambers: ')
nambers = list(map(int, user.split()))
nambers_sort(nambers)
 """


# Напиши програму, яка приймає 3 числа і виводить їх у порядку зростання.
# 🧠 Підказка: використай sorted().
""" 
def sort_nambers(nambers):
    nambers.sort()
    print('Введи три числа: ', nambers)


nambers_input = input('веди три числа: ')
nambers = list(map(int, nambers_input.split()))
sort_nambers(nambers)
 """

""" time fanktion """


""" import datetime
now = datetime.datetime.now()
print(now)
 """


""" from datetime import datetime

def new_time(time):
    if time == 'new time':
        now = datetime.now()
        print(now.time())
    else:
        print("Введіть 'new time', щоб побачити час.")


user_input = input('time: ')
new_time(user_input)
 """

"""
current_datetime = datetime.now()
 print(current_datetime.year)
print(current_datetime.month)
print(current_datetime.day)
print(current_datetime.hour)
print(current_datetime.minute)
print(current_datetime.second)
print(current_datetime.microsecond)
print(current_datetime.tzinfo)

 """

""" 
from datetime import datetime

# Створення об'єкта datetime
now = datetime.now()

# Отримання номера дня тижня
day_of_week = now.weekday()

# Поверне число від 0 (понеділок) до 6 (неділя)
print(f"Сьогодні: {day_of_week}")  
 """


""" from datetime import datetime

def get_days_from_today(date):
    now = datetime.now()
    nambers = datetime.now() + now
    print (date.now() and nambers)


nam = 5
get_days_from_today(nam) """


""" import random

def get_numbers_ticket(min, max, quantity):
    if min.random() >= 1 and max.random() <= 1000: """