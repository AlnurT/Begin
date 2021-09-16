"""Задача 5. Наименьший делитель
Дано натуральное число n>1. Напишите функцию, которая находит его наименьший делитель, отличный от 1."""


def least_divisor(n):
    score = 2
    while n % score != 0:
        score += 1
    return score


def main():
    number = int(input("Введите число: "))

    print("Наименьший делитель, отличный от единицы:", least_divisor(number))


if __name__ == "__main__":
    main()
