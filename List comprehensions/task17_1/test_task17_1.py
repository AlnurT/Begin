from task17_1.task17_1 import search_for_vowels

vowels = frozenset("абеёиоуыэюя")


def test_vowels_is_in_the_text():
    assert search_for_vowels(vowels, "ВАй ты!") == ["а", "ы"]


def test_vowels_isnt_in_the_text():
    assert search_for_vowels(vowels, "Вй т!") == []


def test_empty_text():
    assert search_for_vowels(vowels, "") == []
