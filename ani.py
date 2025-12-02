""" import turtle


def move(a):
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)


def color(a, color):
    turtle.color(color)
    turtle.begin_fill()
    move(a)
    turtle.end_fill()

turtle.speed(1)
color(18, "red")
turtle.goto(150, 150)
 """


""" def anime_stor(library):
    for i in library:
        if len(library) < 3:
            print(f"nambers, {i}")

anime = input("anime: ")
anime_stor(anime) """



""" 
def calculator_plas(nambers, plas, nambers2):
    if plas == '+':
        kake = nambers + nambers2
        print(f'{kake}')


def calculator_minus(nambers, minus, nambers2):
    if minus == '-':
        kake = nambers - nambers2
        print(f'{kake}')

def calculator_mal(nambers, mal, nambers2):
    if mal == '*':
        kake = nambers * nambers2
        print(f'{kake}')

def calculator_getalt(nambers, getalt, nambers2):
    if getalt == '/':
        kake = nambers / nambers2
        print(f'{kake}')

 """

""" 
namber_imput = int(input('namber: '))
namber_imput2 = int(input('namber2: '))
namber_nam = input('+, -, *, /: ')

if namber_nam == '+':
    kake = namber_imput + namber_imput2
    print(f'{kake}')

elif namber_nam == '-':
    kake = namber_imput - namber_imput2
    print(f'{kake}')

elif namber_nam == '*':
    kake = namber_imput * namber_imput2
    print(f'{kake}')

elif namber_nam == '/':
    kake = namber_imput / namber_imput2
    print(f'{kake}')

 """

""" 
import random

nambers = random.randint(1, 109)

for age in range(nambers):
    if age < 18:
        print("не доступно")
        break
    elif age >= 18:
        print("доступ є")
        break
    elif age > 90:
        print("помилка")
        break
 """

""" class Solution:
    def romanToInt(self, s: str) -> int: #self  аргумент — це сам об’єкт
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        total = 0 
        for i in range(len(s)):
            # значення поточного символу
            v = values[s[i]]

            if i + 1 < len(s) and v < values[s[i + 1]]:
                total -= v
            else:
                total += v

        return total """

""" class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for ch in s:
            # якщо відкрита дужка — кладемо в стек
            if ch in '([{':
                stack.append(ch)
            else:
                # якщо стек пустий або верх не підходить — неправильно
                if not stack or stack[-1] != pairs[ch]:
                    return False
                # все ок, прибираємо відповідну відкриту
                stack.pop()

        # якщо стек пустий — всі дужки закрились
        return len(stack) == 0
 """