"""Задача 3. Клетки
В научной лаборатории выводят и тестируют новые виды клеток.  Есть список из N этих клеток, где элемент списка — это
показатель эффективности, а индекс списка — это ранг клетки. Учёные отбирают клетки по следующему принципу:  если
эффективность клетки меньше её ранга, то эта клетка не подходит.

Напишите программу, которая выводит на экран те элементы списка, значения которых меньше их индекса.

Пример:

Кол-во клеток: 5
Эффективность 1 клетки: 3
Эффективность 2 клетки: 0
Эффективность 3 клетки: 6
Эффективность 4 клетки: 2
Эффективность 5 клетки: 10


Неподходящие значения: 0 2"""


def cell_selection(number: int, efficiency: list) -> str:
    low_efficiency = ""
    for rank in range(number):
        if rank + 1 > efficiency[rank]:
            low_efficiency += str(efficiency[rank]) + " "
    return low_efficiency


def main():
    number = int(input("Кол-во клеток: "))
    efficiency = []
    for rank in range(number):
        print(f"Эффективность {rank + 1} клетки: ", end="")
        efficiency.append(int(input()))

    print(f"\n\nНеподходящие значения: {cell_selection(number, efficiency)}")


if __name__ == "__main__":
    main()
