def convert_length(value, from_unit, to_unit):
    # Словарь с коэффициентами преобразования длины
    length_units = {
        "meters": 1,            # Базовая единица — метры
        "kilometers": 0.001,   # 1 метр = 0.001 километров
        "miles": 0.000621371   # 1 метр = 0.000621371 миль
    }

    # Проверка на наличие выбранных единиц в словаре
    if from_unit not in length_units or to_unit not in length_units:
        raise ValueError("Invalid units for length conversion")

    # Конвертация из исходной единицы в метры
    value_in_meters = value / length_units[from_unit]
    # Конвертация из метров в целевую единицу
    converted_value = value_in_meters * length_units[to_unit]
    return converted_value


def convert_weight(value, from_unit, to_unit):
    # Словарь с коэффициентами преобразования веса
    weight_units = {
        "grams": 1000,         # 1 килограмм = 1000 грамм
        "kilograms": 1,       # Базовая единица — килограммы
        "pounds": 2.20462     # 1 килограмм = 2.20462 фунтов
    }

    # Проверка на наличие выбранных единиц в словаре
    if from_unit not in weight_units or to_unit not in weight_units:
        raise ValueError("Invalid units for weight conversion")

    # Конвертация из исходной единицы в килограммы
    value_in_kilograms = value / weight_units[from_unit]
    # Конвертация из килограммов в целевую единицу
    converted_value = value_in_kilograms * weight_units[to_unit]
    return converted_value


def convert_temperature(value, from_unit, to_unit):
    # Проверка и конвертация температуры для различных пар единиц
    if from_unit == "celsius" and to_unit == "fahrenheit":
        return (value * 9/5) + 32  # Конвертация Цельсия в Фаренгейт
    elif from_unit == "celsius" and to_unit == "kelvin":
        return value + 273.15      # Конвертация Цельсия в Кельвин
    elif from_unit == "fahrenheit" and to_unit == "celsius":
        return (value - 32) * 5/9  # Конвертация Фаренгейта в Цельсий
    elif from_unit == "fahrenheit" and to_unit == "kelvin":
        return (value - 32) * 5/9 + 273.15  # Конвертация Фаренгейта в Кельвин
    elif from_unit == "kelvin" and to_unit == "celsius":
        return value - 273.15      # Конвертация Кельвина в Цельсий
    elif from_unit == "kelvin" and to_unit == "fahrenheit":
        return (value - 273.15) * 9/5 + 32  # Конвертация Кельвина в Фаренгейт
    else:
        raise ValueError("Invalid units for temperature conversion")
