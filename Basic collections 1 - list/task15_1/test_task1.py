from task15_1.task1 import list_odd_numbers


def test_number_is_odd():
    assert list_odd_numbers(9) == [1, 3, 5, 7, 9]


def test_number_is_even():
    assert list_odd_numbers(8) == [1, 3, 5, 7]
