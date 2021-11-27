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


def is_weight_more_than_200(weight: int) -> bool:
    return weight > 200


def sort_list_weight(weight_list: list) -> list:
    weight_list.sort(reverse=True)
    return weight_list


def show_number_of_new_container(sorted_weight_list: list, new_weight: int) -> int:
    for container in enumerate(sorted_weight_list):
        if new_weight > container[1]:
            return container[0] + 1
    return len(sorted_weight_list) + 1


def main():
    number_of_containers = int(input("Кол-во контейнеров: "))
    weight_list = []
    for container in range(number_of_containers):
        weight = int(input("Введите вес контейнера: "))
        while is_weight_more_than_200(weight):
            weight = int(input("\nВес контейнера привыщает 200 кг, введите другой вес!"
                                   "\nВведите вес контейнера: "))
        weight_list.append(weight)
        print(f"Вес {container + 1} контейнера: {weight}")

    print("\nОтсортированный список контейнеров:")
    sorted_weight_list = sort_list_weight(weight_list)
    for container in enumerate(sorted_weight_list):
        print(f"Вес {container[0] + 1} контейнера: {container[1]}")

    new_weight = int(input("\nВведите вес нового контейнера: "))
    while is_weight_more_than_200(new_weight):
        new_weight = int(input("\nВес нового контейнера привыщает 200 кг, введите другой вес!"
                               "\nВведите вес нового контейнера: "))

    print(
        f"Номер, куда встанет новый контейнер: {show_number_of_new_container(sorted_weight_list, new_weight)}"
    )


if __name__ == "__main__":
    main()
