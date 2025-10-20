# Задача 2. (Базовая)
# Тема: Использование стандартных модулей. Напишите программу, которая:
# Использует модуль random для генерации случайного числа от 1 до 100.
# Выводит текущую дату и время, используя модуль datetime.

print("Задание №2.\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

import random
from datetime import datetime

random_num = random.randint(1, 100)
print(f"Случайное число: {random_num}")

now_datetime = datetime.now()

fmt_date = now_datetime.strftime("%d.%m.%Y %H:%M:%S")
print(f"Текущая дата и время: {fmt_date}")
