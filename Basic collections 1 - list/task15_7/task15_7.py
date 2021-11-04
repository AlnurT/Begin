"""Задача 7. Контейнеры

Контейнеры на складе лежат в ряд в порядке невозрастания своей массы (в килограммах).
На склад привезли ещё один контейнер, который также нужно положить на определённое место.
Напишите программу, которая получает на вход невозрастающую последовательность натуральных чисел,
означающих массу каждого контейнера в ряду. После этого вводится число X — масса нового контейнера.
Программа выводит номер, под которым будет лежать новый контейнер. Если в ряде есть контейнеры с одинаковой массой,
такой же, как у нового, то его нужно положить после них.

Обеспечьте контроль ввода: все числа не превышают 200.

Пример:

Кол-во контейнеров: 8
Введите вес контейнера: 165
Введите вес контейнера: 163
Введите вес контейнера: 160
Введите вес контейнера: 160
Введите вес контейнера: 157
Введите вес контейнера: 157
Введите вес контейнера: 155
Введите вес контейнера: 154


Введите вес нового контейнера: 162


Номер, куда встанет новый контейнер: 3
"""


def sorted_list_weight(weight_list: list) -> list:
    weight_list.sort(reverse=True)
    return weight_list


def number_of_new_container(new_weight_list: list, new_weight: int) -> int:
    count = 1
    while new_weight < new_weight_list[count - 1]:
        count += 1
    return count


def main():
    number_of_containers = int(input("Кол-во контейнеров: "))
    count = 1
    weight_list = []
    while count <= number_of_containers:
        weight = int(input("Введите вес контейнера: "))
        if weight <= 200:
            weight_list.append(weight)
            count += 1
        else:
            print("Превышен вес контейнера!")

    print()
    new_weight_list = sorted_list_weight(weight_list)
    for count in range(number_of_containers):
        print(f"Вес {count + 1} контейнера: {new_weight_list[count]}")

    new_weight = int(input("\nВведите вес нового контейнера: "))

    print(
        f"Номер, куда встанет новый контейнер: {number_of_new_container(new_weight_list, new_weight)}"
    )


if __name__ == "__main__":
    main()
