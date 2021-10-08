"""Задача 4. Число наоборот 3
Пользователь вводит два вещественных числа — N и K.
Напишите программу, которая отдельно заменяет сначала целую часть на число,
которое получается из исходного записью его цифр в обратном порядке, затем то же самое делает с дробной частью.
После этого числа складываются и сумма выводится на экран."""


def reverse_number(number: str, part: int) -> str:
    return number.split(".")[part][::-1]


def assembly_number(number: str) -> float:
    return float(reverse_number(number, 0) + "." + reverse_number(number, 1))


def main():
    n = input("Введите первое число: ")
    k = input("Введите второе число: ")

    print(f"\nПервое число наоборот: {assembly_number(n)}")
    print(f"Второе число наоборот: {assembly_number(k)}")
    print(f"Сумма: {assembly_number(n) + assembly_number(k)}")


if __name__ == "__main__":
    main()
