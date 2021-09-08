"""Задача 4. Число наоборот 3
Пользователь вводит два вещественных числа — N и K.
Напишите программу, которая отдельно заменяет сначала целую часть на число,
которое получается из исходного записью его цифр в обратном порядке, затем то же самое делает с дробной частью.
После этого числа складываются и сумма выводится на экран."""

def main():
    n = float(input('Введите первое число: '))
    k = float(input('Введите второе число: '))

    def reverse(number: int) -> int:
        reverse_number = 0
        while number != 0:
            reverse_number = reverse_number * 10 + number % 10
            number //= 10
        return reverse_number

    def()

    def separation_and_assembly(number: float) -> float:
        from decimal import Decimal
        int_number = int(number)
        fractional_number = Decimal(number - int_number)
        count_fractional_number = 0
        while fractional_number != 0:
            count_fractional_number += 1
            fractional_number //= 10
        new_number = reverse(int_number) + reverse(fractional_number) /  count_fractional_number
        return new_number

    new_n = separation_and_assembly(n)
    new_k = separation_and_assembly(k)
    print('\nПервое число наоборот:', new_n)
    print('Второе число наоборот:', new_k)
    print('Сумма:', new_n + new_k)


main()