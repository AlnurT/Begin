"""Задача 1. Генерация списка
Дано целое число N. Напишите программу, которая формирует список из нечётных чисел от 1 до N."""


def list_odd_numbers(number: int) -> list:
    return list(range(1, number + 1, 2))


def main():
    number = int(input("Введите целое число N: "))

    print(f"Список нечетных чисел: {list_odd_numbers(number)}")


if __name__ == "__main__":
    main()
