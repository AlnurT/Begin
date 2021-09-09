"""Задача 4. Число наоборот 3
Пользователь вводит два вещественных числа — N и K.
Напишите программу, которая отдельно заменяет сначала целую часть на число,
которое получается из исходного записью его цифр в обратном порядке, затем то же самое делает с дробной частью.
После этого числа складываются и сумма выводится на экран."""

def main():
    n = input('Введите первое число: ')
    k = input('Введите второе число: ')

    def reverse(number: str) -> str:
        number = int(number)
        reverse_number = 0
        while number != 0:
            reverse_number = reverse_number * 10 + number % 10
            number //= 10
        reverse_number = str(reverse_number)
        return reverse_number


    def separation_and_assembly(number: str) -> float:
        int_numb_bool = True
        int_number = ''
        fractional_number = ''
        for symbol in number:
            if symbol != '.' and int_numb_bool == True:
                int_number += symbol
            elif symbol == '.':
                int_numb_bool = False
            elif int_numb_bool == False:
                fractional_number += symbol
        new_number = float(reverse(int_number) + '.' + reverse(fractional_number))
        return new_number

    new_n = separation_and_assembly(n)
    new_k = separation_and_assembly(k)
    print('\nПервое число наоборот:', new_n)
    print('Второе число наоборот:', new_k)
    print('Сумма:', new_n + new_k)


main()