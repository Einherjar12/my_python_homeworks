# Задание №1. Простая арифметика. Напишите программу, которая запрашивает
# у пользователя два числа и выводит их сумму, разность, произведение и частное.

print("Задание №1.\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    print(f"{num1} + {num2} = {num1 + num2}")
    print(f"{num1} - {num2} = {num1 - num2}")
    print(f"{num1} * {num2} = {num1 * num2}")

    if num2 == 0:
        raise ZeroDivisionError("Ошибка: деление на ноль невозможно!")
    else:
        print(f"{num1} / {num2} = {num1 / num2:.3f}")

except ValueError:
    print("Ошибка: введено нечисловое значение!")
except ZeroDivisionError as e:
    print(e)

# Задание №2. Чётное или нечётное? Напишите программу, которая принимает число и
# выводит "Чётное", если число делится на 2, и "Нечётное" в противном случае.

print("\nЗадание №2.\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

try:
    number = int(input("Введите целое число: "))

    if number % 2 == 0:
        print("Чётное")
    else:
        print("Нечётное")

except ValueError:
    print("Ошибка: введите корректное целое число!")

# Задание №3. Факториал числа. Напишите функцию, которая вычисляет факториал
# числа n (произведение всех чисел от 1 до n). Пример: Ввод: 5 → Вывод: 120 (1×2×3×4×5).

print("\nЗадание №3.\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")


def factorial_n(n):
    if n < 0:
        raise ValueError("Ошибка: факториал отрицательного числа не определён!")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


try:
    num_str = input("Введите целое неотрицательное число: ")

    num_float = float(num_str)
    if not num_float.is_integer():
        raise ValueError("Ошибка: введено дробное число!")

    number = int(num_float)
    print(f"Факториал числа {number}: {factorial_n(number)}")

except ValueError as e:
    print(e)

# Задание №4. Поиск максимального числа в списке.
# Напишите функцию, которая принимает список чисел и возвращает наибольшее из них.
# Пример: Ввод: [3, 7, 2, 9, 1] → Вывод: 9.

print("\nЗадание №4.\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")


def find_max(num):
    return max(num)


numbers = [3, 7, 2, 9, 1]
print(find_max(numbers))

# Задание №5. Палиндром. Напишите функцию, которая проверяет,
# является ли строка палиндромом (читается одинаково слева направо и справа налево).
# Пример: Ввод: "топот" → Вывод: True Ввод: "python" → Вывод: False.

print("\nЗадание №5.\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")


def is_palindrome(line):
    new_line = "".join(i.lower() for i in line if i.isalnum())
    return new_line == new_line[::-1]


print(is_palindrome("топот"))
print(is_palindrome("Каза!!к"))
print(is_palindrome("А роза упала на лапу Азора"))

# Задание №6. Подсчёт гласных. Напишите функцию, которая считает количество гласных
# букв (a, e, i, o, u) в строке. Пример: Ввод: "Hello, World!" → Вывод: 3(e, o, o).

print("\nЗадание №6.\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")


def count_vowels(line):
    vowels = 'aeiou'
    vowels_in_line = [i for i in line.lower() if i in vowels]
    return len(vowels_in_line), vowels_in_line


text = "Hello, World!"
count, letters = count_vowels(text)
print(f"{count} ({', '.join(letters)})")

# Задание №7. Генератор паролей. Напишите функцию, которая генерирует случайный пароль
# заданной длины (используйте буквы, цифры и символы).
# Пример: Ввод: 8 → Вывод: "aB3$k9Lm" (случайная комбинация)/.

print("\nЗадание №7.\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

import random
import string


def generate_password(length):
    if not isinstance(length, int) or length <= 0:
        raise ValueError("Длина пароля должна быть положительным целым числом!")

    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password


try:
    print(generate_password(8))
except ValueError as e:
    print(e)

# Задание №8. Разворот списка. Напишите функцию, которая переворачивает список без использования
# встроенного метода .reverse(). Пример: Ввод: [1, 2, 3, 4] → Вывод: [4, 3, 2, 1].

print("\nЗадание №8.\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")


def reverse_list(lst):
    return lst[::-1]


print(reverse_list([1, 2, 3, 4]))

# Задание №9. Фильтрация списка. Напишите функцию, которая принимает список чисел и возвращает
# новый список, содержащий только чётные числа.
# Пример: Ввод: [1, 2, 3, 4, 5, 6] → Вывод: [2, 4, 6].

print("\nЗадание №9.\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")


def find_even_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]

    return even_numbers


print(find_even_numbers([1, 2, 3, 4, 5, 6]))

# Задание №10. Калькулятор времени. Напишите функцию, которая принимает количество секунд и
# возвращает строку в формате "Дни:Час:Мин:Сек".
# Пример: Ввод: 100000 → Вывод: "1:3:46:40" (1 день, 3 часа, 46 минут, 40 секунд).

print("\nЗадание №10.\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")


def convert_seconds(seconds):
    if not isinstance(seconds, int) or seconds < 0:
        raise ValueError("Время должно быть неотрицательным целым числом!")

    days = seconds // (24 * 60 * 60)
    hours = (seconds % 24 * 60 * 60) // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    return f"{days}:{hours}:{minutes}:{seconds}"


try:
    print(convert_seconds(100000))
    print(convert_seconds(-70))
except ValueError as e:
    print(e)
