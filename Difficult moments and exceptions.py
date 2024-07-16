def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for number in numbers:
        try:
            if isinstance(number, (int, float)):
                result += number
            else:
                incorrect_data += 1
                print(f"Некорректный тип данных для подсчёта суммы - {number}")
        except ValueError:
            incorrect_data += 1
            print(f"Некорректный тип данных для подсчёта суммы - {number}")
    return result, incorrect_data


def calculate_average(numbers):
    try:
        if isinstance(numbers, (list, tuple, str)):
            total_sum, incorrect_data = personal_sum(numbers)
            if incorrect_data > 0:
                return None
            return total_sum / len(numbers) if len(numbers) > 0 else 0
        else:
            print('В numbers записан некорректный тип данных')
            return None
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None


print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
