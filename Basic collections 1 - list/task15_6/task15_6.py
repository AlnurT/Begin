"""Мы пишем программу — анализатор слов, чтобы потом, возможно, использовать её для тренировки нейросети,
которая будет генерировать нужный нам текст.

Пользователь вводит слово. Напишите программу, которая считает количество уникальных букв в слове.
Уникальные буквы — это те, которые встречаются всего один раз.

Пример 1:

Введите слово: привет
Кол-во уникальных букв: 6

Пример 2:

Введите слово: лава
Кол-во уникальных букв: 2"""


def count_unique_symbols_in(word: str) -> int:
    unique_symbols = {}
    count = 0
    for symbol in word:
        unique_symbols[symbol] = unique_symbols.get(symbol, 0) + 1
    for _, value in unique_symbols.items():
        if value == 1:
            count += 1
    return count


def main():
    word = input("Введите слово: ")

    print(f"Кол-во уникальных букв: {count_unique_symbols_in(word)}")


if __name__ == "__main__":
    main()
