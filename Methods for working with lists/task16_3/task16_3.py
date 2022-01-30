"""Задача 3. Детали

В базе данных магазина всякой всячины хранится список названий деталей и их стоимостей:
shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], ['седло', 1500], ['рама', 12000],
['обод', 2000], ['шатун', 200], ['седло', 2700]]

Продавец решил, что считать количество и стоимость деталей вручную не очень удобно,
поэтому решил попросить помощи у программиста, чтобы оптимизировать этот процесс.
Напишите программу, которая запрашивает у пользователя деталь, считает их количество, а также общую стоимость.

Пример:

Название детали: седло

Кол-во деталей - 3
Общая стоимость - 4500
"""


def find_the_number_of_details_and_their_cost(shop: list, detail: str) -> tuple:
    number_of_details = 0
    cost_of_details = 0
    for detail_in_shop in shop:
        if detail == detail_in_shop[0]:
            number_of_details += 1
            cost_of_details += detail_in_shop[1]
    return number_of_details, cost_of_details


def main():
    shop = [
        ["каретка", 1200],
        ["шатун", 1000],
        ["седло", 300],
        ["педаль", 100],
        ["седло", 1500],
        ["рама", 12000],
        ["обод", 2000],
        ["шатун", 200],
        ["седло", 2700],
    ]
    detail = input("Название детали: ")

    number_of_details = find_the_number_of_details_and_their_cost(shop, detail)[0]
    cost_of_details = find_the_number_of_details_and_their_cost(shop, detail)[1]
    print(f"Кол-во деталей - {number_of_details}")
    print(f"Общая стоимость - {cost_of_details}")


if __name__ == "__main__":
    main()
