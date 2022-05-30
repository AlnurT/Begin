"""Задача 8. Развлечение
N палочек выставили в один ряд, пронумеровав их слева направо числами от 1 до N.
Затем по этому ряду бросили K камней, при этом i-й камень сбил все палки с номерами от L_i до R_i включительно.
Определите, какие палки остались стоять на месте.

Напишите программу, которая получает на вход количество палок N и количество бросков K.
Далее идёт K пар чисел Left_i, Right_i, при этом 1 ≤ Left_i ≤ Right_i ≤ N.

Программа должна вывести последовательность из N символов, где j-й символ есть “I”,
если j-я палка осталась стоять, или “.”, если j-я палка была сбита.

Пример:
Количество палок: 10
Количество бросков: 3
Бросок 1. Сбиты палки с номера 8
по номер 10.
Бросок 2. Сбиты палки с номера 2
по номер 5.
Бросок 3. Сбиты палки с номера 3
по номер 6.

Результат: I.....I...
"""


def knock_down_sticks(sticks: str, left_i: int, right_i: int) -> str:
    return sticks[: left_i - 1] + "." * (right_i - left_i + 1) + sticks[right_i:]


def main():
    n = int(input("Кол-во палок: "))
    k = int(input("Кол-во бросков: "))
    sticks = "|" * n

    for throw in range(k):
        print(f"\nБросок {throw + 1}.")
        left_i = int(input("Сбиты палки с номера "))
        right_i = int(input("по номер "))
        sticks = knock_down_sticks(sticks, left_i, right_i)

    print(f"\nРезультат: {sticks}")


if __name__ == "__main__":
    main()