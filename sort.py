""" import time
import os 
import random

def show(arr):
    show_lst = [[" " for _ in range(len(arr)) for _ in range(max(arr))]]
    for i in range(len((arr))):
        for j in  range(arr[i]):
            show_lst[j][i] = "*"
    show_lst.reverse()

    for row in show_lst:
        print(" ".join(row))

    
    time.sleep(0.1)
    os.system("cls")

def sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] >= arr(j + 1):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                show(arr)
 

lst = [random.randint(1,12) for _ in range(20)]

sort(lst) """
""" 
import time
import os
import random

def show(arr):
    show_lst = [[" " for _ in range(len(arr))] for _ in range(max(arr))]

    for i in range(len(arr)):
        for j in range(arr[i]):
            show_lst[j][i] = "*"

    show_lst.reverse()

    for row in show_lst:
        print(" ".join(row))

    time.sleep(0.1)
    os.system("cls")  # для Windows

def sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                show(arr)

lst = [random.randint(1, 12) for _ in range(20)]
sort(lst) """

""" message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
search = "r"
result = 0
for words in message:
    #ти перебираєш слітеру р типу кажеш чи є р в повідомлені 
    if words == search:
       # ти робиш зміну для результату
       result = result + 1
    
         """

""" some_list = ["apple", "banana", "cherry"]
for index, value in enumerate(some_list):
    print(index, value)

    0 apple
1 banana
2 cherry

 """

""" list1 = ["зелене", "стигла", "червоний"]
list2 = ["яблуко", "вишня", "томат"]
for number, letter in zip(list1, list2):
    print(number, letter)
 """

""" numbers = {
    1: "one",
    2: "two",
    3: "three"
}
# виведе числа keys()
for key in numbers:
    print(key)

    # виводить слова values()
for val in numbers.values():
    print(val)
# комбо 
for key, value in numbers.items():
    print(key, value)
 """

""" def invite_to_event(username):
    user_nam = input(f"Dear {username}, we have the honour to invite you to our event")
    return user_nam


invite_to_event() """

""" def get_fullname(first_name, last_name, middle_name):
    first_name = input("your first name: ")
    middle_name = input("your middle name: ")
    last_name = input("your last name: ")

    if first_name == " ":
        input("your first name: ")
    elif middle_name == " ":
        input("your middle name: ")
    elif last_name == " ":
        input("your last name: ")

    return (f"{first_name} {middle_name} {last_name}") """




""" def get_fullname(first_name, last_name, middle_name=""):
    if middle_name.strip():
        return f"{first_name} {middle_name} {last_name}"
    else:
        return f"{first_name} {last_name}" """



""" def format_string(string, length):
    if len(string) >= length:
        return string
    else:
        spaces = (length - len(string)) // 2
        return " " * spaces + string
     """

""" def first(size, *args):
    len(args)
    return args + size


def second(size, **kwargs):
    len(kwargs)
    return kwargs + size """

""" def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


def number_of_groups(n, k):
    return factorial(n) // (factorial(n - k) * factorial(k)) """

""" import keyboard
import pyautogui
import threading
import time

spamming = False

def on():
    global spamming
    spamming = not spamming


def spam():
    global spamming
    while True:
        if spamming:
            pyautogui.typewrite("здорова", interval=0.5)
            pyautogui.press("enter")
        else:
            time.sleep(0.1)

threading.Thread(target=spam, daemon=True).start()

keyboard.add_hotkey("f7", on )
keyboard.wait() """



import pyautogui
import threading
import time
from pynput import keyboard

spamming = False


def toggle_spam():
    global spamming
    spamming = not spamming
    print(f"Spamming: {'ON' if spamming else 'OFF'}")


def spam():
    while True:
        if spamming:
            pyautogui.write("здорова", interval=0.05)
            pyautogui.press("enter")
            time.sleep(1)
        else:
            time.sleep(0.1)


def on_press(key):
    try:
        if key == keyboard.Key.p:
            toggle_spam()
        elif key == keyboard.Key.p:
            print("Exiting...")
            return False
    except:
        pass


# Потік спаму
threading.Thread(target=spam, daemon=True).start()

print("F7 - toggle spam | F8 - exit")

# Слухач клавіш
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()