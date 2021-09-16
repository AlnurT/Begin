"""Задача 4. Число наоборот 3
Пользователь вводит два вещественных числа — N и K.
Напишите программу, которая отдельно заменяет сначала целую часть на число,
которое получается из исходного записью его цифр в обратном порядке, затем то же самое делает с дробной частью.
После этого числа складываются и сумма выводится на экран."""


def reverse(number: str) -> str:
    reverse_number = ""
    for symbol in number:
        reverse_number = symbol + reverse_number
    return reverse_number


def separation_and_assembly(number: str) -> float:
    int_numb_bool = True
    int_number = ""
    fractional_number = ""
    for symbol in number:
        if symbol != "." and int_numb_bool:
            int_number += symbol
        elif symbol == ".":
            int_numb_bool = False
        elif not int_numb_bool:
            fractional_number += symbol
    return float(reverse(int_number) + "." + reverse(fractional_number))


def summa_new_numbers(new_n: float, new_k: float) -> float:
    return new_n + new_k


def main():
    n = input("Введите первое число: ")
    k = input("Введите второе число: ")

    new_n = separation_and_assembly(n)
    new_k = separation_and_assembly(k)

    print(f"\nПервое число наоборот: {new_n}")
    print(f"Второе число наоборот: {new_k}")
    print(f"Сумма: {summa_new_numbers(new_n, new_k)}")


if __name__ == "__main__":
    main()
