"""Задача 3. Сумма и разность
Напишите две функции: первая принимает одно целое положительное число N и находит сумму всех цифр числа N;
вторая принимает число N и считает количество цифр в числе. В ответе выводится разность суммы чисел и количества."""


def summa(n: str) -> int:
    return sum(map(int, n))


def counting_numerals(n: str) -> int:
    return len(n)


def main():
    n = input("Введите число: ")

    print(f"\nСумма цифр: {summa(n)}")
    print(f"Кол-во цифр в числе: {counting_numerals(n)}")
    print(f"Разность суммы и кол-ва цифр: {summa(n) - counting_numerals(n)}")


if __name__ == "__main__":
    main()
