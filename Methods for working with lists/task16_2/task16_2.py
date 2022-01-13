"""Задача 2. Шеренга

Два класса стоят в две отдельные шеренги.
В каждом классе ученики выстроены по росту (по возрастанию): в одном классе от 160 см до 176 см с шагом 2,
во втором классе — от 162 см до 180 см с шагом 3.
Спустя какое-то время два класса объединяют в одну шеренгу и тоже выстраивают их по возрастанию.

Напишите программу, которая генерирует списки роста для каждого в классе,
затем объединяет их в один список и сортирует его в порядке возрастания.
Выведите отсортированный список на экран.
"""


def create_list(min_height: int, max_height: int, step: int) -> list:
    return list(range(min_height, max_height + 1, step))


def main():
    min_height_1 = 160
    max_height_1 = 176
    step_1 = 2
    min_height_2 = 162
    max_height_2 = 180
    step_2 = 3

    class_a = create_list(min_height_1, max_height_1, step_1)
    class_b = create_list(min_height_2, max_height_2, step_2)
    print(f"Список роста учеников класса А: {class_a}")
    print(f"Список роста учеников класса А: {class_b}")

    class_a_b = class_a + class_b
    class_a_b.sort()
    print(f"Список роста учеников класса А: {class_a_b}")


if __name__ == "__main__":
    main()
