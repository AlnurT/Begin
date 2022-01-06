"""Задача 1. Страшный код

Вашему другу, который тоже начал изучать Python, преподаватель дал такую задачу: есть три списка — основной и два побочных.
В основном лежат элементы [1, 5, 3], а в побочных [1, 5, 1, 5] и [1, 3, 1, 5, 3, 3] соответственно.

Первый побочный закидывается в основной, там считается количество цифр 5, количество выводится на экран,
и затем они удаляются из основного списка. После этого в основной закидывается второй побочный список,
там считается количество цифр 3 и выводится на экран. В конце также выводится и сам список.

Результат работы программы:

Кол-во цифр 5 при первом объединении: 3
Кол-во цифр 3 при втором объединении: 4
Итоговый список: [1, 3, 1, 1, 1, 3, 1, 5, 3, 3]
"""


def count_the_number_of_digits(main_list: list, digit: int) -> int:
    return main_list.count(digit)


def delete_digit(main_list: list, number_of_digits: int, digit: int) -> list:
    for _ in range(number_of_digits):
        main_list.remove(digit)
    return main_list


def main():
    main_list = [1, 5, 3]
    first_list = [1, 5, 1, 5]
    second_list = [1, 3, 1, 5, 3, 3]

    main_list.extend(first_list)
    number_of_digits_5 = count_the_number_of_digits(main_list, 5)
    delete_digit(main_list, number_of_digits_5, 5)
    print(f"Кол-во цифр 5 при первом объединении: {number_of_digits_5}")

    main_list.extend(second_list)
    number_of_digits_3 = count_the_number_of_digits(main_list, 3)
    print(f"Кол-во цифр 3 при втором объединении: {number_of_digits_3}")

    print(f"Итоговый список: {main_list}")


if __name__ == "__main__":
    main()
