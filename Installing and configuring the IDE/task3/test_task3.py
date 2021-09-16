from task3.task3 import counting_numerals, difference_summa_and_counting_numbers, summa


def test_summa_of_numerals():
    assert summa("1567") == 19


def test_counting_numerals():
    assert counting_numerals("1567") == 4


def test_difference_summa_and_counting_numbers():
    assert difference_summa_and_counting_numbers(19, 4) == 15
