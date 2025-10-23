# Задание №1. К уже реализованному классу «Автомобиль» добавьте
# возможность упаковки и распаковки данных с использованием json и pickle.

print("Задание №1.\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

import json
import pickle


class Car:
    def __init__(self, model="", year=0, manufacturer="", volume=0, color="", price=0):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.volume = volume
        self.color = color
        self.price = price

    def input_data(self):
        self.model = input("Введите название модели: ")
        while True:
            try:
                self.year = int(input("Введите год выпуска: "))
                if self.year < 1884 or self.year > 2027:
                    raise ValueError("Неверный год выпуска.")
                break
            except ValueError as e:
                print("Ошибка:", e)

        self.manufacturer = input("Введите производителя: ")

        while True:
            try:
                self.volume = float(input("Введите объем двигателя: "))
                if self.volume <= 0:
                    raise ValueError("Объем двигателя должен быть положительным числом.")
                break
            except ValueError as e:
                print("Ошибка:", e)

        self.color = input("Введите цвет машины: ")

        while True:
            try:
                self.price = float(input("Введите цену: "))
                if self.price < 0:
                    raise ValueError("Цена не может быть отрицательной.")
                break
            except ValueError as e:
                print("Ошибка:", e)

    def output_data(self):
        print("\nИнформация о машине:")
        print(f"Название модели : {self.model}")
        print(f"Год выпуска : {self.year}")
        print(f"Производитель : {self.manufacturer}")
        print(f"Объем двигателя : {self.volume}")
        print(f"Цвет машины : {self.color}")
        print(f"Цена : {self.price}")

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_manufacturer(self):
        return self.manufacturer

    def get_volume(self):
        return self.volume

    def get_color(self):
        return self.color

    def get_price(self):
        return self.price

    def save_to_json(self, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.__dict__, f, ensure_ascii=False, indent=4)

    @classmethod
    def load_from_json(cls, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        car = cls()
        car.__dict__.update(data)
        return car

    def save_to_pickle(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def load_from_pickle(cls, filename):
        with open(filename, 'rb') as f:
            car = pickle.load(f)
        return car


car1 = Car()
car1.input_data()
car1.output_data()

car1.save_to_json("car.json")
car_from_json = Car.load_from_json("car.json")
print("\nЗагружено из JSON:")
car_from_json.output_data()

car1.save_to_pickle("car.pkl")
car_from_pickle = Car.load_from_pickle("car.pkl")
print("\nЗагружено из Pickle:")
car_from_pickle.output_data()

# Задание №2. К уже реализованному классу «Книга» добавьте возможность
# упаковки и распаковки данных с использованием json и pickle.

print("\nЗадание №2.\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

import json
import pickle


class Book:
    def __init__(self):
        self.name = input("Введите название книги: ")
        self.year = int(input("Введите год выпуска: "))
        self.publisher = input("Введите издателя: ")
        self.style = input("Введите жанр: ")
        self.author = input("Введите автора: ")
        self.price = int(input("Введите цену: "))

    def output_data(self):
        print("\nИнформация о книге:")
        print(f"Название книги : {self.name}")
        print(f"Год выпуска : {self.year}")
        print(f"Издатель : {self.publisher}")
        print(f"Жанр : {self.style}")
        print(f"Автор : {self.author}")
        print(f"Цена : {self.price}")

    def get_name(self):
        return self.name

    def get_year(self):
        return self.year

    def get_publisher(self):
        return self.publisher

    def get_style(self):
        return self.style

    def get_author(self):
        return self.author

    def get_price(self):
        return self.price

    def save_to_json(self, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.__dict__, f, ensure_ascii=False, indent=4)

    @classmethod
    def load_from_json(cls, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        book = cls.__new__(cls)
        book.__dict__.update(data)
        return book

    def save_to_pickle(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def load_from_pickle(cls, filename):
        with open(filename, 'rb') as f:
            book = pickle.load(f)
        return book


book1 = Book()
book1.output_data()

book1.save_to_json("book.json")
book_from_json = Book.load_from_json("book.json")
print("\nЗагружено из JSON:")
book_from_json.output_data()

book1.save_to_pickle("book.pkl")
book_from_pickle = Book.load_from_pickle("book.pkl")
print("\nЗагружено из Pickle:")
book_from_pickle.output_data()

# Задание №3. К уже реализованному классу «Стадион» добавьте
# возможность упаковки и распаковки данных с использованием json и pickle.

print("\nЗадание №3.\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

import json
import pickle


class Stadium:
    def __init__(self, name="", open_date="", country="", city="", capacity=0):
        self.name = name
        self.open_date = open_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def input_data(self):
        self.name = input("Введите название стадиона: ")
        self.open_date = input("Введите дату открытия (01.01.2000): ")
        self.country = input("Введите страну: ")
        self.city = input("Введите город: ")
        self.capacity = int(input("Введите вместимость стадиона: "))

    def output_data(self):
        print("\nИнформация о стадионе:")
        print(f"Название: {self.name}")
        print(f"Дата открытия: {self.open_date}")
        print(f"Страна: {self.country}")
        print(f"Город: {self.city}")
        print(f"Вместимость: {self.capacity} человек")

    def get_name(self):
        return self.name

    def get_open_date(self):
        return self.open_date

    def get_country(self):
        return self.country

    def get_city(self):
        return self.city

    def get_capacity(self):
        return self.capacity

    def save_to_json(self, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.__dict__, f, ensure_ascii=False, indent=4)

    @classmethod
    def load_from_json(cls, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        stadium = cls.__new__(cls)
        stadium.__dict__.update(data)
        return stadium

    def save_to_pickle(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def load_from_pickle(cls, filename):
        with open(filename, 'rb') as f:
            stadium = pickle.load(f)
        return stadium


stadium1 = Stadium()
stadium1.input_data()
stadium1.output_data()

print("\nНазвание стадиона: ", stadium1.get_name())

stadium1.save_to_json("stadium.json")
stadium_from_json = Stadium.load_from_json("stadium.json")
print("\nЗагружено из JSON:")
stadium_from_json.output_data()

stadium1.save_to_pickle("stadium.pkl")
stadium_from_pickle = Stadium.load_from_pickle("stadium.pkl")
print("\nЗагружено из Pickle:")
stadium_from_pickle.output_data()
