"""Задача 10. Симметричная последовательность



Что нужно сделать
Последовательность чисел называется симметричной, если она одинаково читается как слева направо, так и справа налево.
Например, следующие последовательности являются симметричными:

1 2 3 4 5 4 3 2 1
1 2 1 2 2 1 2 1

Пользователь вводит последовательность из N чисел. Напишите программу, которая определяет,
какое минимальное количество и каких чисел надо приписать в конец этой последовательности, чтобы она стала симметричной.

Пример 1:
Кол-во чисел: 5
Число: 1
Число: 2
Число: 1
Число: 2
Число: 2

Последовательность: [1, 2, 1, 2, 2]
Нужно приписать чисел: 3
Сами числа: [1, 2, 1]

Пример 2:
Кол-во чисел: 5
Число: 1
Число: 2
Число: 3
Число: 4
Число: 5

Последовательность: [1, 2, 3, 4, 5]
Нужно приписать чисел: 4
Сами числа: [4, 3, 2, 1]
"""


def assign_numbers_for_list_symmetry(
    list_numbers: list, list_new_numbers: list
) -> tuple:
    insert_index = len(list_numbers)
    for num in list_numbers:
        if list_numbers == list_numbers[::-1]:
            break
        list_numbers.insert(insert_index, num)
        list_new_numbers.insert(0, num)
    return len(list_new_numbers), list_new_numbers


def main():
    print("Введите числа через пробел:", end=" ")
    list_numbers = list(map(int, input().split()))
    print(f"\nПоследовательность: {list_numbers}")

    amount_new_numbers = assign_numbers_for_list_symmetry(list_numbers, [])[0]
    list_new_numbers = assign_numbers_for_list_symmetry(list_numbers, [])[1]
    print(f"Нужно приписать чисел: {amount_new_numbers}")
    print(f"Сами числа: {list_new_numbers}")


if __name__ == "__main__":
    main()
