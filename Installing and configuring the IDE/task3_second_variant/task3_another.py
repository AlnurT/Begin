"""Задача 3. Сумма и разность
Напишите две функции: первая принимает одно целое положительное число N и находит сумму всех цифр числа N;
вторая принимает число N и считает количество цифр в числе. В ответе выводится разность суммы чисел и количества."""

def main():
    n = input('Введите число: ')

    def summa(n: str) -> int:
        summ = 0
        for symbol in n:
            summ += int(symbol)
        return summ

    def counting_numbers(n: str) -> int:
        count = 0
        for symbol in n:
            count += 1
        return count

    print('\nСумма цифр:', summa(n))
    print('Кол-во цифр в числе:', counting_numbers(n))
    print('Разность суммы и кол-ва цифр:', summa(n) - counting_numbers(n))

main()