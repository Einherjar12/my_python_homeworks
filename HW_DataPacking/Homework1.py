# Задание №1. Есть некоторый словарь, который хранит названия
# стран и столиц. Название страны используется в качестве
# ключа, название столицы в качестве значения. Необходимо
# реализовать: добавление данных, удаление данных, поиск
# данных, редактирование данных, сохранение и загрузку
# данных (используя упаковку и распаковку).

print("Задание №1.\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

import pickle

countries = {
    "Россия": "Москва",
    "Франция": "Париж",
    "Германия": "Берлин"
}


def add_country(country_dict, country, capital):
    country_dict[country] = capital
    print(f"Добавлено: {country} - {capital}")


def delete_country(country_dict, country):
    if country in country_dict:
        del country_dict[country]
        print(f"Удалено: {country}")
    else:
        print("Страна не найдена.")


def find_country(country_dict, country):
    capital = country_dict.get(country)
    if capital:
        print(f"Столица страны {country}: {capital}")
    else:
        print("Страна не найдена.")


def edit_country(country_dict, country, new_capital):
    if country in country_dict:
        country_dict[country] = new_capital
        print(f"Столица страны {country} изменена на {new_capital}.")
    else:
        print("Страна не найдена.")


def save_data(filename, data):
    with open(filename, "wb") as file:
        pickle.dump(data, file)
    print("Данные сохранены.")


def load_data(filename):
    try:
        with open(filename, "rb") as file:
            data = pickle.load(file)
        print("Данные загружены.")
        return data
    except FileNotFoundError:
        print("Файл не найден.")
        return None


def main():
    filename = "countries.pkl"

    current_countries = countries.copy()

    while True:
        print("\n--- Меню ---")
        print("1. Добавить страну")
        print("2. Удалить страну")
        print("3. Найти столицу")
        print("4. Изменить столицу")
        print("5. Показать все страны")
        print("6. Сохранить данные")
        print("7. Загрузить данные")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            country = input("Введите название страны: ")
            capital = input("Введите столицу: ")
            add_country(current_countries, country, capital)

        elif choice == "2":
            country = input("Введите название страны для удаления: ")
            delete_country(current_countries, country)

        elif choice == "3":
            country = input("Введите название страны для поиска: ")
            find_country(current_countries, country)

        elif choice == "4":
            country = input("Введите название страны: ")
            new_capital = input("Введите новую столицу: ")
            edit_country(current_countries, country, new_capital)

        elif choice == "5":
            if current_countries:
                print("\nСписок стран и столиц:")
                for c, cap in current_countries.items():
                    print(f"{c} — {cap}")
            else:
                print("Список пуст.")

        elif choice == "6":
            save_data(filename, current_countries)

        elif choice == "7":
            loaded = load_data(filename)
            if loaded is not None:
                current_countries = loaded

        elif choice == "0":
            print("Выход из программы.")
            break

        else:
            print("Неверный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main()

# Задание №2. Есть некоторый словарь, который хранит названия музыкальных
# групп(исполнителей) и альбомов. Название группы используется в качестве
# ключа, название альбомов в качестве значения. Необходимо реализовать:
# добавление данных, удаление данных, поиск данных, редактирование данных,
# сохранение и загрузку данных (используя упаковку и распаковку).

print("\nЗадание №2.\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

import pickle

music_library = {
    "Linkin Park": "Meteora",
    "Muse": "Absolution",
    "Queen": "A Night at the Opera"
}


def add_band(library, band, album):
    library[band] = album
    print(f"Добавлено: {band} — {album}")


def delete_band(library, band):
    if band in library:
        del library[band]
        print(f"Удалено: {band}")
    else:
        print("Группа не найдена.")


def find_band(library, band):
    album = library.get(band)
    if album:
        print(f"Альбом группы {band}: {album}")
    else:
        print("Группа не найдена.")


def edit_band(library, band, new_album):
    if band in library:
        library[band] = new_album
        print(f"Альбом группы {band} изменён на {new_album}.")
    else:
        print("Группа не найдена.")


def save_data(filename, data):
    with open(filename, "wb") as file:
        pickle.dump(data, file)
    print("Данные сохранены.")


def load_data(filename):
    try:
        with open(filename, "rb") as file:
            data = pickle.load(file)
        print("Данные загружены.")
        return data
    except FileNotFoundError:
        print("Файл не найден.")
        return None


def main():
    filename = "music_library.pkl"
    current_library = music_library.copy()

    while True:
        print("\n--- МЕНЮ ---")
        print("1. Добавить группу и альбом")
        print("2. Удалить группу")
        print("3. Найти альбом по группе")
        print("4. Изменить альбом")
        print("5. Показать все группы")
        print("6. Сохранить данные")
        print("7. Загрузить данные")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            band = input("Введите название группы: ")
            album = input("Введите название альбома: ")
            add_band(current_library, band, album)

        elif choice == "2":
            band = input("Введите название группы для удаления: ")
            delete_band(current_library, band)

        elif choice == "3":
            band = input("Введите название группы для поиска: ")
            find_band(current_library, band)

        elif choice == "4":
            band = input("Введите название группы: ")
            new_album = input("Введите новый альбом: ")
            edit_band(current_library, band, new_album)

        elif choice == "5":
            if current_library:
                print("\nСписок групп и альбомов:")
                for b, a in current_library.items():
                    print(f"{b} — {a}")
            else:
                print("Список пуст.")

        elif choice == "6":
            save_data(filename, current_library)

        elif choice == "7":
            loaded = load_data(filename)
            if loaded is not None:
                current_library = loaded

        elif choice == "0":
            print("Выход из программы.")
            break

        else:
            print("Неверный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main()
