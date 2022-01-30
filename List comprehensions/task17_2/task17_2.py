"""Задача 2. Генерация

Пользователь вводит целое число N. Напишите программу, которая генерирует список из N чисел,
на чётных местах в нём стоят единицы, а на нечётных — числа, равные остатку от деления своего номера на 5.

Пример:

Введите длину списка: 10
Результат: [1, 1, 1, 3, 1, 0, 1, 2, 1, 4]
"""


def list_of_units_and_remainders(list_length: int) -> list:
    return [(1 if item % 2 == 0 else item % 5) for item in range(list_length)]


def main():
    list_length = int(input("Введите длину списка: "))

    print(f"Рузультат: {list_of_units_and_remainders(list_length)}")


if __name__ == "__main__":
    main()
