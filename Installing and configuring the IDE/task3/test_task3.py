from task3.task3 import counting_numerals, summa


def test_summa_of_numerals():
    assert summa("1567") == 19


def test_counting_numerals():
    assert counting_numerals("1567") == 4
