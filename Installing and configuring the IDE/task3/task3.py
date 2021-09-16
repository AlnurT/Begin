"""Задача 3. Сумма и разность
Напишите две функции: первая принимает одно целое положительное число N и находит сумму всех цифр числа N;
вторая принимает число N и считает количество цифр в числе. В ответе выводится разность суммы чисел и количества."""


def summa(n: str) -> int:
    summ = 0
    for symbol in n:
        summ += int(symbol)
    return summ


def counting_numerals(n: str) -> int:
    return len(n)


def difference_summa_and_counting_numbers(summ: int, counting_numbers: int) -> int:
    return summ - counting_numbers


def main():
    n = input("Введите число: ")

    print(f"\nСумма цифр: {summa(n)}")
    print(f"Кол-во цифр в числе: {counting_numerals(n)}")
    print(
        f"Разность суммы и кол-ва цифр: {difference_summa_and_counting_numbers(summa(n), counting_numerals(n))}"
    )


if __name__ == "__main__":
    main()
