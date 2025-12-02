""" def alt(jahre):
    print(f"bist du {jahre}")

alt(18)
alt(52)
 """

"""  import time

print("На іншу любов, іншу любов")
time.sleep(4)
print("Сльози всі вже пролито")
time.sleep(3)
print("На іншу любов, іншу любов")
time.sleep(2)
print("Сльози всі вже пролито, о-о")
 """ 

""" import random
namber = random.randint(1, 43)
print("zeil ist", namber) """


""" import time

print("Мы выросли там где нет нормы морали")
time.sleep(0.3)
print("По спирали вниз, над нами стая птиц кружит")
time.sleep(3)
print("И я прошу не вспоминай меня пока я здесь, пока я еще жив")
 """


""" import time
import random
namber = random.randint(1, 19)
def untericht(lernen):
    print(f"в мене {lernen}",)

untericht(namber)
time.sleep(3)
untericht("матиматика")  """




# Введення (отримання даних)
""" vlados = input("Введіть ваше ім'я: ")

# Перетворення (обробка даних)
hallo = (f"Привіт, {vlados}!")

# Виведення (виведення даних)
print(hallo) """


""" begrüsung = input("Введіть ваше ім'я: ")

hallo = (f"Hallo schon mit dir kennen zu lehrnen {begrüsung}")

print(hallo) """


""" import time

namber = input("Write down the number: ")

namber_teip = (f"Thank you for the number {namber}")

print(namber_teip) """

""" name = input("name: ")

hello = (f"hallo { Тут можна використовувати функцію }")
print(hello) """

""" mein_name = input("Введи своє ім’я: ")
mein_age = int(input("Введи свій вік: "))   # переводимо у число
wird = "Через 5 років"
age_5 = mein_age + 5

print(f"Привіт, {mein_name}! Тобі {mein_age} років.")
print(f"{wird} тобі буде {age_5}.")
 """

""" text = "Привіт, Владислав!"

print(len(text))          # довжина рядка
print(text.upper())       # ВЕЛИКІ букви
print(text.lower())       # маленькі букви 
print(text.replace("Владислав", "Python"))  # заміна частини рядка
print(text[0])            # доступ до символу
print(text[-1])           # останній символ
print(text[0:7])          # зріз (від 0 до 5 індексу)
print(text.startswith("Привіт"))  # True перевіряє, чи рядок починається з вказаного слова
print(text.endswith("!"))         # True endswith("!") → перевіряє, чи рядок закінчується на вказаний символ
print("Влад" in text)     # True Оператор in → перевіряє, чи підрядок входить у рядок. Якщо "Влад" є в text, то результат True.
"""

""" numbers = [10, 20, 30, 40]

print(numbers[0])      # 10
numbers.append(50)     # додає елемент
numbers.remove(20)     # видаляє елемент
print(len(numbers))    # довжина списку
print(numbers[::-1])   # розворот
print(len(numbers))
numbers.remove(20) # не може мати 2 обєкта і копією з одинаковим числом
numbers.append(11)
numbers.append(88)
numbers.append(48)
numbers.remove(30)
print(numbers)  """

""" coords = (10, 20)
print(coords[0])   # 10
"""

""" fruits = {"яблуко", "банан", "яблуко"}

fruits.add("груша")# add слово додає
fruits.add("чай")
fruits.remove("яблуко")
print(fruits)    """


""" student = {
    "name": "Влад",
    "age": 17,
    "grade": "A",
    "sistem_generation": ""
}

print(student["name"])          # Влад
student["age"] = 18             # зміна
print(student.keys())           # усі ключі
print(student.values())         # усі значення
student["grade"] = ("ahahhahahhahha")
student["sistem_generation"] = "I feel very good."
print(student["sistem_generation"]) """

""" sentence = "Я люблю Python і програмування"
words = sentence.split()       # розбити рядок на список
print(words)                   # ['Я', 'люблю', 'Python', 'і', 'програмування']

joined = " ".join(words)       # зібрати назад у рядок
print(joined)                  # Я люблю Python і програмування 
 """
""" user_text = input("user: ")
user = "admin"
user_guest = "guest"

if user_text == user:
    print("Доступ дозволено")
elif user_text == user_guest: # == Перевіряє чи мають обидві змінні однаковий зміст
    print("Обмежений доступ")
else:                         # is Перевіряє чи це той самий 
    print("Доступ заборонено") #обєкт (одна й та сама коробка в памяті)?
 """
""" from tkinter import *
root = Tk()

root.title("window")
root.mainloop()

from tkinter import *

root = Tk()
root.title("Window")
 """

# приклад шаблону
# Щоб перевірити щось в input можна просто використати текст якій потрібен 
# наприклад як в цьому випадку gest і можна перевіряти
# чи є пуста строчка в воду  якщо там нічого не треба 
""" user = input("Введіть ім'я: ")
password = input("Введіть пароль: ")
gest = "gest"

if user is "admin" and password == "python123":
    print("Доступ дозволено")

elif user == "gest" and password == "":
    print("доступ обмежений")

else:
    print("Неправильне ім’я або пароль") """


""" 💡 ТЗ: Перевірка температури та пори року

Напиши програму, яка запитує температуру (число) і пору року (зима, літо, осінь, весна).
Виведи:
"Холодно" якщо температура нижче 10 або це зима
"Тепло" якщо температура більше 20 і це літо
"Прохолодно" якщо температура між 10 і 20
Інакше — "Невизначено"
💬 Підказка: Використай if, elif, else, and, or. """
""" 
time = int(input("температура: "))

if time < 10:
    print("Холодно")
elif time > 20:
    print("Тепло")
elif time >= 10 or 20:
    print("Прохолодно")
else:
    print("Невизначено") """


""" namber = int(input("nambers: "))

lange = len(str(namber))
if lange == 3 and namber % 2 == 0:
    print("erorr") """


""" def greet(name):
    # твій код тут
    print('hallo' + ' ' + name)

user_inport = input('name: ')
greet(user_inport) """

""" def add_numbers(a, b):
    # твій код тут
    nambers = a + b
    print(f'{nambers}')

user_input = int(input('nambers: '))
user_input2 = int(input('nambers2: '))
add_numbers(user_input, user_input2) """

""" def check_number(num):
    # твій код тут
    if num % 2 == 0:
        print(f'{num}: парне число')
    elif not num % 2 == 0:
        print(f'{num}: не парне число')

user_input = int(input('nambers: '))
check_number(user_input)
 """
""" 
Напиши функцію, яка обчислює факторіал числа """
""" def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i  # множимо всі числа від 1 до n
    return result

# користувач вводить число
num = int(input("Введи число: "))
print(f"Факторіал числа {num}:", factorial(num))
 """

""" 
def greet(name):
    print("hallo" + " " + name)

user_name = input("your names:")
greet(user_name) """

""" def print_max(a, b):
    if a > b:
        print(a, 'максимально')
    elif a == b:
        print(a, 'дорівнює', b)
    elif a and b % 2 == 0:
        print("парне число")
    else:
        print(b, 'максимально')

print_max(3, 4)  # пряма передача значень

x = int(input("nambers: "))
y = int(input("nambers: "))
print_max(x, y)  # передача змінних у якості аргументів
 """

""" 
num = [11, 2, 6, 1, 8, 88, 120, 123]

def nambere_nan(nambers):
    print(max(nambers))
    
nambere_nan(num) """

""" 
def greet(name: str) -> str:
    if name.isupper():
        print('з велткої літери')
    return (f"Привіт, {name}!")
greeting = input('your names: ')
print(greeting)  # Виведе: Привіт, Олексій!
 """


""" 
def user_nik(names):
    if not names:
        print("i need nemes: ")
    else:
        print(f"{names} привіт бро")


user_nemes = input("user names: ")
user_nik(user_nemes) """
""" 
def string_to_codes(string: str) -> dict:
    # Ініціалізація словника для зберігання кодів
    codes = {}  
    # Перебір кожного символу в рядку
    for ch in string:  
        # Перевірка, чи символ вже є в словнику
        if ch not in codes:
            # Додавання пари символ-код в словник  
            codes[ch] = ord(ch)  
    return codes


result = string_to_codes("Hello world!")
print(result)
 """

""" my_drim = 18

def drim(my):
    global my_drim
    if my < my_drim:
        print("роби")
    else:
        print("ти зміг")


home = int(input("nambers"))
drim(home) """

""" from datetime import datetime

def get_days_from_today(date):
 
    try:
       
        target_date = datetime.strptime(date, '%Y-%m-%d').date()
        
        today = datetime.today().date()
        
        delta = (target_date - today).days
        return delta
    except ValueError:
        
        print("Неправильний формат дати. Використовуйте 'РРРР-ММ-ДД'.")
        return None


print(get_days_from_today("2021-10-09"))
 """

""" def print_numbers(n):
    for i in range(1, n + 1):
        print(i)

print_numbers(5)
 """

""" def multiplication_table(n):
    for i in range(1, 11): # Тому що рахується з нуля 
                            # і нам було потрібно пробувати числа через які ми будемо рахувати 
        print(f"{n} x {i} = {n * i}") # А тут ми рахуємо за допомогою {n * i}


user_input = int(input("yours nambers: "))
multiplication_table(user_input) """

# 🧠 Завдання 3: Підрахунок голосних
# ТЗ:
# Створи функцію count_vowels(text),
# яка підраховує кількість голосних літер (a, e, i, o, u) у слові або реченні.



""" def count_vowels(text):
    vowels = ('a', 'e', 'i', 'o', 'u')
    text_vowels = 0

    for letter in text.lower():
        if letter in vowels:
            text_vowels += 1
    
    print(f"Кількість голосних: {text_vowels}")


user_input = input('text: ')
count_vowels(user_input) """


""" def filter_lower(words):
    list_text = []
    for i in words:
        lowe_words = i.lower()
        if len(lowe_words) > 3 and lowe_words[0] == "a":
            list_text.append(lowe_words)
    return list_text

input_list = ["Apple", "Art", "Banana", "area", "Ant", "Car"]
print(filter_lower(input_list)) """
""" 
for char in "Hello 123":
    if char.isdigit():
        print(f"'{char}' - це цифра")
    else:
        print(f"'{char}' - не цифра")
 """


""" def min_namber(namber):
    user_namber = namber[0]# припускаємо, що перший елемент — мінімальний
    for i in namber:
        if i < user_namber:
            user_namber = i
    print(user_namber) # виводимо мінімальне значення

user_nan = [5, 3, 7, 2, 9]
min_namber(user_nan) """


""" def nambers_sort(nambers):
    for i in nambers:
        if i > 10:
            print('ja')
        else:
            print('nein')


user_input = input('namberss: ')
numbers_list = list(map(int, user_input.split()))
nambers_sort(numbers_list) """

""" class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for row in range(numRows):
            # Починаємо кожен рядок з 1
            current = [1] * (row + 1)

            # Заповнюємо внутрішні елементи (якщо вони є)
            for j in range(1, row):
                current[j] = triangle[row - 1][j - 1] + triangle[row - 1][j]

            triangle.append(current)

        return triangle

generate(3)
 """


""" import tkinter as tk 

modal = 0

def one_click():
    global modal
    modal += 1
    print(modal)

root = tk.Tk()

btn = tk.Button(root,text="Нажми меня",command=one_click)
btn.pack()


root.mainloop() """

import tkinter as tk

mate = 0

def cliker_click():
    global mate
    mate += 1
    btn.config(text=str(mate))


root = tk.Tk()

btn = tk.Button(root, text="0", command=cliker_click)

btn.pack()

root.mainloop()