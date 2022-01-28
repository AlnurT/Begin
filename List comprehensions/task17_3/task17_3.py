"""Задача 3. Случайные соревнования

Мы хотим протестировать работу электронной таблицы для участников некоторых соревнований.
Есть два списка (то есть две команды) по 20 участников в каждом.
В этих списках хранятся очки каждого участника (это вещественные числа с двумя знаками после точки, например 4.03).
Участник одной команды соревнуется с участником другой команды под таким же номером.
То есть первый соревнуется с первым, второй — со вторым и так далее.

Напишите программу, которая генерирует два списка участников (по 20 элементов)
из случайных вещественных чисел (от 5 до 10). Для этого найдите подходящую функцию из модуля random.
Затем сгенерируйте третий список, в котором окажутся только победители из каждой пары.

Пример:

Первая команда: [7.86, 6.76, 9.97, 9.08, 5.45, 6.9, 8.65, 5.17, 8.17, 5.06, 7.56, 7.1, 7.18, 8.25, 5.53,
7.95, 8.91, 7.11, 8.29, 9.52]

Вторая команда: [7.13, 5.7, 8.89, 5.36, 5.62, 9.46, 5.82, 8.67, 8.41, 7.0, 5.31, 7.8, 9.93, 7.76, 7.4,
8.26, 7.94, 5.71, 7.89, 7.77]

Победители тура: [7.86, 6.76, 9.97, 9.08, 5.62, 9.46, 8.65, 8.67, 8.41, 7.0, 7.56, 7.8, 9.93, 8.25,
7.4, 8.26, 8.91, 7.11, 8.29, 9.52]
"""

import random


def create_list_of_thehighest_scores(
    first_team_scores: list, second_team_scores: list, number_of_participants: int
) -> list:
    return [
        (
            first_team_scores[score]
            if first_team_scores[score] >= second_team_scores[score]
            else second_team_scores[score]
        )
        for score in range(number_of_participants)
    ]


def main():
    number_of_participants = 20
    first_team_scores = [
        round(random.uniform(5, 10), 2) for _ in range(number_of_participants)
    ]
    second_team_scores = [
        round(random.uniform(5, 10), 2) for _ in range(number_of_participants)
    ]
    winners = create_list_of_thehighest_scores(
        first_team_scores, second_team_scores, number_of_participants
    )

    print(f"Первая команда: {first_team_scores}")
    print(f"Вторая команда: {second_team_scores}")
    print(f"Победители тура: {winners}")


if __name__ == "__main__":
    main()
