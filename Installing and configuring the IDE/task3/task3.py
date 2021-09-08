"""Задача 3. Сумма и разность
Напишите две функции: первая принимает одно целое положительное число N и находит сумму всех цифр числа N;
вторая принимает число N и считает количество цифр в числе. В ответе выводится разность суммы чисел и количества."""

def main():
    n = int(input('Введите число: '))

    def summa(n: int) -> int:
        summ = 0
        while n != 0:
            summ += n % 10
            n //= 10
        return summ

    def counting_numbers(n: int) -> int:
        count = 0
        while n != 0:
            count += 1
            n //= 10
        return count

    print('\nСумма цифр:', summa(n))
    print('Кол-во цифр в числе:', counting_numbers(n))
    print('Разность суммы и кол-ва цифр:', summa(n) - counting_numbers(n))

main()