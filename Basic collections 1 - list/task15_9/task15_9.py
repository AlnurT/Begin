"""Задача 9. Анализ слова 2

Мы продолжаем писать программы — анализаторы для текста, и теперь от нас требуется реализовать код,
с помощью которого можно будет определять, является ли слово палиндромом — словом,
которое одинаково читается слева направо и справа налево.

Пример 1:

Введите слово: мадам
Слово является палиндромом


Пример 2:

Введите слово: abccba
Слово является палиндромом


Пример 3:

Введите слово: abbd
Слово не является палиндромом
"""


def is_word_palindrome(word: str) -> bool:
    return word == word[::-1]


def main():
    word = input("Введите слово: ")
    if is_word_palindrome(word):
        print("Слово является палиндромом")
    else:
        print("Слово не является палиндромом")


if __name__ == "__main__":
    main()
