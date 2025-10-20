# Задание №3. Тема: Создание своего пакета
# Создайте структуру пакета:
# my_package/
#     __init__.py
#     calculator.py
#     greeting.py
#
# В calculator.py определите функции add(a, b) и multiply(a, b).
# В greeting.py определите функцию say_hello(name).
# В файле вне пакета (main.py) импортируйте обе функции и используйте их.

print("Задание №3.\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

from my_package.calculator import add, multiply
from my_package.greeting import say_hello

result_add = add(6, 4)
result_multiply = multiply(5, 7)
result_greeting = say_hello("Владимир")

print(f"Сумма: {result_add}")
print(f"Произведение: {result_multiply}")
print(result_greeting)
