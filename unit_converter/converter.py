from conversion_utils import convert_length, convert_weight, convert_temperature

def main():
    # Словарь с параметрами для каждой конверсии: тип, метка и функция преобразования
    conversion_options = {
        "1": ("length", "Длина", convert_length),
        "2": ("weight", "Вес", convert_weight),
        "3": ("temperature", "Температура", convert_temperature)
    }

    while True:
        print("\nДобро пожаловать в конвертер единиц измерения!")
        # Печать доступных опций для пользователя
        for key, (conv_type, label, _) in conversion_options.items():
            print(f"{key}. {label}")
        print("4. Выход")

        # Получение выбора пользователя
        choice = input("Выберите тип конвертации (1-4): ")

        if choice in conversion_options:
            # Получение параметров для выбранной опции
            conv_type, _, conversion_func = conversion_options[choice]
            # Вызов обработчика конверсии
            handle_conversion(conv_type, conversion_func)
        elif choice == "4":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

def handle_conversion(conversion_type, conversion_func):
    # Словарь с доступными единицами для каждого типа конверсии
    units_dict = {
        "length": {
            "1": "meters",
            "2": "kilometers",
            "3": "miles"
        },
        "weight": {
            "1": "grams",
            "2": "kilograms",
            "3": "pounds"
        },
        "temperature": {
            "1": "celsius",
            "2": "fahrenheit",
            "3": "kelvin"
        }
    }

    # Получение словаря единиц для выбранного типа конверсии
    units = units_dict[conversion_type]
    # Ввод значения для преобразования
    value = float(input("\nВведите значение: "))
    print("Доступные единицы:")
    # Печать доступных единиц
    for key, unit in units.items():
        print(f"{key}. {unit}")

    # Ввод исходной и целевой единиц с проверкой по ключам
    from_unit_key = input("Введите номер исходной единицы: ").strip()
    to_unit_key = input("Введите номер целевой единицы: ").strip()

    if from_unit_key in units and to_unit_key in units:
        from_unit = units[from_unit_key]
        to_unit = units[to_unit_key]
        try:
            # Вызов функции преобразования
            result = conversion_func(value, from_unit, to_unit)
            print(f"{value} {from_unit} равно {result} {to_unit}.")
        except ValueError as e:
            # Обработка ошибки, если выбранные единицы недействительны
            print(e)
    else:
        # Вывод сообщения об ошибке при некорректном выборе
        print("Неверный выбор единицы.")

if __name__ == "__main__":
    main()