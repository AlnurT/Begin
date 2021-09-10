"""Задача 3. Сумма и разность
Напишите две функции: первая принимает одно целое положительное число N и находит сумму всех цифр числа N;
вторая принимает число N и считает количество цифр в числе. В ответе выводится разность суммы чисел и количества."""

def main():
    n = input('Введите число: ')

    def summa(n: str) -> str:
        summ = 0
        for symbol in n:
            summ += int(symbol)
        print(f'\nСумма цифр: {summ}')
        return summ

    def counting_numbers(n: str) -> str:
        count = 0
        for symbol in n:
            count += 1
        print(f'Кол-во цифр в числе: {count}')
        return count

    sub = summa(n) - counting_numbers(n)
    print(f'Разность суммы и кол-ва цифр: {sub}')
    return sub

if __name__ == '__main__':
    main()