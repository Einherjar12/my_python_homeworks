# Задание №5. Тема: Установка и использование внешних пакетов
# Установите библиотеку requests через pip.
# Напишите скрипт, который отправляет GET-запрос
# на сайт https://jsonplaceholder.typicode.com/posts/1 .
# Распечатайте статус-код ответа и содержимое в формате JSON.

print("Задание №5.\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

import requests
import json

url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    response = requests.get(url)
    response.raise_for_status()

    print(f"Статус-код: {response.status_code}")
    data = response.json()
    print("Ответ в формате JSON:")
    print(json.dumps(data, indent=4, ensure_ascii=False))

except requests.exceptions.RequestException as e:
    print(f"Произошла ошибка при запросе: {e}")
