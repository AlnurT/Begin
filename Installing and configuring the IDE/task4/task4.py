"""Задача 4. Число наоборот 3
Пользователь вводит два вещественных числа — N и K.
Напишите программу, которая отдельно заменяет сначала целую часть на число,
которое получается из исходного записью его цифр в обратном порядке, затем то же самое делает с дробной частью.
После этого числа складываются и сумма выводится на экран."""


from decimal import Decimal


def reverse_number(number: str) -> Decimal:
    return Decimal(number.split(".")[0][::-1] + "." + number.split(".")[1][::-1])


def main():
    n = input("Введите первое число: ")
    k = input("Введите второе число: ")

    print(f"\nПервое число наоборот: {reverse_number(n)}")
    print(f"Второе число наоборот: {reverse_number(k)}")
    print(f"Сумма: {reverse_number(n) + reverse_number(k)}")


if __name__ == "__main__":
    main()
