"""Задача 8. Бегущие цифры

Вы пишете программу для маленького табло, в котором циклически повторяется один и тот же текст или числа —
прямо как в каком-нибудь метро, автобусах или трамваях.

Дан список из N элементов и целое число K. Напишите программу,
которая циклически сдвигает элементы списка вправо на K позиций.
Используйте минимально возможное количество операций присваивания.

Пример 1:

Сдвиг: 1
Изначальный список: [1, 2, 3, 4, 5]
Сдвинутый список: [5, 1, 2, 3, 4]


Пример 2:

Сдвиг: 3
Изначальный список: [1, 4, -3, 0, 10]
Сдвинутый список: [-3, 0, 10, 1, 4]
"""


def shift_of_elements_in_list(listt: list, shift: int) -> list:
    if shift > len(listt):
        shift -= len(listt)
        shift_of_elements_in_list(listt, shift)
    elif shift < 0:
        shift += len(listt)
        shift_of_elements_in_list(listt, shift)
    else:
        return listt[shift - 1:] + listt[:shift - 1]


def main():
    shift = int(input("Сдвиг: "))
    number = int(input("Кол-во элементов в списке: "))
    listt = []
    for _ in range(number):
        print(f"Введите {_ + 1} элемент списка: ", end="")
        listt.append(int(input()))

    print(f"Изначальный список: {listt}")
    print(f"Сдвинутый список: {shift_of_elements_in_list(listt, shift)}")


if __name__ == "__main__":
    main()
