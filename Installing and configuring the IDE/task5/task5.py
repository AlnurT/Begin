"""Задача 5. Наименьший делитель
Дано натуральное число n>1. Напишите функцию, которая находит его наименьший делитель, отличный от 1."""


def least_divisor(n):
    if n % 2 == 0:
        return 2
    else:
        for score in range(3, int(n ** 0.5) + 1, 2):
            if n % score == 0:
                return score
    return n


def main():
    number = int(input("Введите число: "))

    print("Наименьший делитель, отличный от единицы:", least_divisor(number))


if __name__ == "__main__":
    main()
