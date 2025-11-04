""" Завдання:
Запроси в користувача два числа та дію (+, -, *, /).
Якщо дія не одна з цих чотирьох — виведи "Невідома операція".
Інакше обчисли результат і виведи.

Підказка:
Комбінуй if, elif, else. """
""" nambers1 = int(input("my nambers1: "))
nambers_maiking = input("(+, -, *, /): ")
nambers = int(input("my nambers2: "))

if nambers_maiking == "+":
    print("namber =", nambers1 + nambers)
elif nambers_maiking == "-":
    print("nambers =", nambers1 - nambers)
elif nambers_maiking == "*":
    print("nambers =", nambers1 * nambers)
elif nambers_maiking == "/":
       if nambers == 0:
        print("Помилка: ділення на нуль!")
       else:
        print("nambers =", nambers1 / nambers)
else:
    print("EROR") """ 
""" 🧩 1. Проверка пароля и имени

Задание:
Напиши программу, которая:
спрашивает имя и пароль,
даёт доступ только если:
имя — "admin" и пароль — "12345",
иначе выводит сообщение об ошибке.
Если имя "guest" или "test", то выводи: "Ограниченный доступ".
Если имя пустое — напиши "Ошибка: имя не указано!".
📘 Подсказка:
Используй and, or, not, if, elif, else. """
""" 
name = input("імя: ")
key = input("пароль: ")

if name == "admin" and key == "12345":
    print ("повний доступ")
elif name == "guest" or "test" and key == "":
    print("Ограниченный доступ")
else:
    print("Ошибка: имя не указано") """



""" ⚙️ 2. Проверка температуры
Задание:
Пользователь вводит температуру на улице.
Если температура больше 25 и меньше 35, вывести "Тепло".
Если меньше 0, вывести "Мороз".
Если не холодно и не жарко (например, от 10 до 25), вывести "Нормально".
В других случаях — "Незвичні погодні умови".
📘 Подсказка:
Используй комбинации and, or, not. """

""" tim_lid = {
    "timlid_name": "timur",
    "timlid_age": 17,
    "timlid_funktion": "зєднати команду"
}
print(tim_lid.keys())

 """

""" # Задаємо конкретне число
num = int(input("nambers:"))

# Перевіряємо кратність
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz") 
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)
 """
""" 
🧩 ТЗ №1 — Вік користувача

Завдання:
Запроси в користувача вік.
Якщо йому більше або дорівнює 18 → "Доступ дозволено".
Якщо менше 18, але є дозвіл батьків (True) → "Доступ дозволено з дозволом".
Інакше → "Доступ заборонено".
Підказка: використай if age >= 18 or parent_permission == True. """

""" 
user_age = int(input("age: "))

if user_age >= 18 :
    print("Доступ дозволено")
elif user_age < 18:
    print("Доступ дозволено з дозволом")
elif user_age == 0:
    print("подайте дані")
    if user_age == -0:
        print("не можливо")
elif user_age >= 100:
    print("подайте дані")
else:
    print(None)  """

""" user_age = int(input("age: "))
parent_permission = input("Є дозвіл батьків? (yes/no): ")

if user_age == 0:
    print("Подайте справжні дані")
elif user_age >= 100:
    print("Неправильний вік")
elif user_age >= 18:
    print("Доступ дозволено")
elif user_age < 18 and parent_permission == "yes":
    print("Доступ дозволено з дозволом")
else:
    print("Доступ заборонено")
 """

""" if x >= 0:
    if y >= 0:  # x > 0, y > 0
        print("Перша чверть")
    else:  # x > 0, y < 0
        print("Четверта чверть")
else:
    if y >= 0:  # x < 0, y > 0
        print("Друга чверть")
    else:  # x < 0, y < 0
        print("Третя чверть")

 """
""" tex = input("tex: ")
msg = "Не було повернено даних"
if not  tex:# якщо воно являється пустишкою за того що not прямо 
    print(msg)# каже якщо в компоненті tex є none то print = "Не було повернено даних" """

""" fruit = "apple"

match fruit:
    case "apple":
        print("This is an apple.")
    case "banana":
        print("This is a banana.")
    case "orange":
        print("This is an orange.")
    case _:
        print("Unknown fruit.")
 """

""" age = int(input('yors nambers: '))


match age:
    case _ if age >= 18:
        print('без обмежень')
    case _ if age >= 16:
        print('з обмеженням')
    case _ if age >= 10:
        print('йди гуляй')
    case _:
        print("це не являється відповідю")

 """

""" products = ["apple", "banana"]
there_is_no = ["milk", "bread", "tomato", "potato"]
it_is = ["eggs", "cheese"]
products_int = input('what products do you need: ')

match products_int:
    case _ if products_int == it_is:
        print ('in stock')
    case _ if products_int == there_is_no:
        print('not available')
    case _ if products_int != products and it_is and there_is_no:
        print("it not produkts")
 """

""" products = ["apple", "banana"]
there_is_no = ["milk", "bread", "tomato", "potato"]
it_is = ["eggs", "cheese"]

products_int = input('What product do you need: ').lower()  # .lower() щоб не було різниці між великими і малими літерами

match products_int:
    case _ if products_int in products:
        print('✅ Product available')
    case _ if products_int in it_is:
        print('🟡 In stock (limited)')
    case _ if products_int in there_is_no:
        print('❌ Not available')
    case _:
        print('🚫 Unknown product')
fom gbt """

""" ehttps://chatgpt.com/share/68fbc1ca-c980-8001-907c-85802965bcb """
        

""" i = 0
while i <= 5:
    print("Число:", i)
    i += 1
 """

""" for i in range(5):
    print("Число:", i)
 """

""" import calendar
year = int(input("Enter year: "))
month = int(input("Enter month: "))
cal = calendar.month(year, month)
print(cal) """

""" products = ['bread', 'apple', 'cheese', 'tomato', 'banana', 'eggs', 'milk', 'potato']

for i in products:
    print(i)
 """
""" alphabet = "abcdefghijklmnopqrstuvwxyz"
for char in alphabet:
    print(char, end=" ")
 """

""" nambers = [1, 3, 12, 49, 32]

for i in nambers:# i це назва переміної
    print(i ** 2) """

""" user_input = input("your text: ")
tex_pruf = len(user_input)
tex = 0
for nambers in user_input:
    if nambers == " ":
        tex += 1

print(f"Загальна кількість символів у рядку: {tex_pruf}")
print(f"Кількість пробілів у рядку: {tex}") """

""" user_input = input("Введіть рядок: ")
vowel_count = 0
consonant_count = 0

vowel = "aeiouаеєиіїоуюя"
consonant = "bcdfghjklmnpqrstvwxyzбвгґджзйклмнпрстфхцчшщ"


for nambers in user_input: #in → перевіряє, чи елемент є в колекції.
    if nambers in vowel:
        vowel_count += 1
    elif nambers in consonant:
        consonant_count += 1

print(f"Кількість голосних {vowel_count}")
print(f"Кількість приголосних {consonant_count}") """


""" user_input = input("Введіть рядок:")

digits_count = 0 
letters_count = 0 
other_count = 0

for char in user_input:
    if char.isdigit():# перевіряє чи є цифри
        digits_count += 1
    elif char.isalpha():# перевіряє чи є літери
        letters_count += 1
    else:
        other_count += 1

print(f"Кількість літер: {letters_count}")
print(f"Кількість цифр: {digits_count}")
print(f"Кількість інших символів: {other_count}") """

""" k = 0
while k < 12:
    k += 1
    
print(k) """

""" while True:
    user_input = input('text: ')
    print(user_input)
    if user_input == "exit":
        break
 """
""" a = 0
while a < 6:
    a = a + 1
    if not a % 2:
        continue
    print(a)
 """

""" user_input = int(input("yours nambers: "))

for nambers in range(user_input):# range це використовується для 
    if nambers % 2 == 0:         #переводу int and input в форму яка понятна для for
        print(f"{nambers} є парним числом.")
    else:
        print(f"{nambers} є непарним числом.")
 """

""" 🧠 Завдання: Змініть код так, щоб він виводив тільки парні числа від 1 до 10. """
""" i = 1
while i <= 10:
    if i % 2 != 0:
        print(f"{i} не парне число")
    i += 1
 """


""" 🧠 Завдання: Зробіть так, щоб програма запитувала в користувача кінцеве число (замість завжди 5). """
""" user_input = int(input('nambers: '))
total = 0
num = 1

while range(user_input) != 5:
    user_input += 1

    if user_input == 5:
        print('Сума:', user_input)
    elif user_input != 5:
        user_input += 1 """

""" 
user_input = int(input("Введіть число: "))
total = 0
num = 1

while num <= user_input:
    total += num
    num += 1

print("Сума:", total)
 """

""" Завдання: Обмежте користувача трьома спробами. Якщо він не вгадає — вивести "Доступ заборонено!".
 """

""" correct_password = "python123"
tries = 0
max_tries = 3

while tries < max_tries:
    password = input("Введіть пароль: ")
    if password == correct_password:
        print("Доступ дозволено!")
        break
    else:
        tries += 1
        if tries < max_tries:
            print(f"Невірний пароль! У вас залишилось {max_tries - tries} спроби.")
        else:
            print("Доступ заборонено! Ви вичерпали всі спроби.")
 """



""" 🧠 Завдання: Додайте підказки:
Виводьте "Занадто мало!", якщо число менше за secret
Виводьте "Занадто багато!", якщо більш """

""" secret = 7
guess = 0

while  secret != guess:
    guess = int(input("Вгадай число (1-10): "))
    if guess < secret:
        print("Занадто мало!")
    elif guess > secret:
        print("Занадто багато!")
    elif guess == ' ':
        print('нічого не має')
    else:
        print("Правильно!")

 """


""" i = 1
while i < 6:
  print(i)
  i += 1 """
""" 
➡️ Завдання: нехай користувач вводить слово, а програма виводить кожну букву з нового рядка. """
""" user_input = input("text: ")

for letter in user_input:
    print(letter)
 """

""" total = int(input("yours nambers: "))
for i in range(total):
    if i % 2 == 0:
        print("Сума:", total)
    elif i % 2 == 1:
          print("none") """
"""     else:
        if i % 2 != 0:
            print("none")
 """

""" 
word = input("Введи слово: ")
vowels = "аеєиіїоуюяAEIOUaeiou"
count = 0
count_20 = 0
for letter in word:
    if letter in vowels:
        count += 1
    elif word != vowels:
        count_20 += 1
print("Кількість голосних:", count)
print("Кількість приголосних:", count_20) """


""" user_nambers = int(input("nambers: "))

for i in range(1, user_nambers):
    if i < 10:
        print(i)
    elif i > 10:
        print("nambers", i) """


""" user_produkts = input("produkts: ")
products = ["apple", "banana", "milk", "bread", "eggs", "cheese", "tomato", "potato"]

found = False  # прапорець, чи знайдено продукт

for i, products in enumerate(products): #enumerate покозує індекс
    if products == user_produkts:
        print(f"{products} має індекс {i}")
        found = True
        break


if not found:
    print("none")

 """

""" 
user_cities = input("yours cities: ")
cities = ["Kyiv", "Lviv", "Odessa", "Dnipro", "Kharkiv"]

found = False  # чи знайдено місто

for i, city in enumerate(cities):
    if city == user_cities:
        print(f"{user_cities} i love my citis{i}")
        found = True
        break


if not found:
    print("None") """

""" students = ["Vlad", "Anna", "Oleh", "Masha"]
subjects = ["Math", "English", "Python", "History"]
grades = [90, 85, 100, 78]


for students, subjects, grades in zip(students, subjects, grades):# коли в нас є масив даних то ми можемо використовувати ці перемені в циклі 
    print(f"{students} отримав {grades} балів з предмету {subjects}") """

""" for i in range(2, 20):
    if i % 3 == 0:    
        print(i)
 """

""" some_list = ["apple", "banana", "cherry"]
for index, value in enumerate(some_list):
    print(index, value)
 """
""" nambers = [1, 2, 3, 4, 5]
for i, nam in enumerate(nambers):
    print(i, nam) """
""" 
list1 = input("have match: ")
list2 = input("fruts: ")
for number, letter in zip(list1, list2):
    print(number)
    print(f"{letter}")
 """

""" numbers = {
    1: "one",
    2: "two",
    3: "three"
}

for key in numbers.keys():
    print(key)
 """
""" 
for val in numbers.values():
    print(val)
 """

