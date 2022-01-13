from task16_1.task16_1 import count_the_number_of_digits, delete_digit


def test_count_the_number_of_digits_5():
    assert count_the_number_of_digits([1, 5, 3, 1, 5, 1, 5], 5) == 3


def test_delete_digit_5():
    assert delete_digit([1, 5, 3, 1, 5, 1, 5], 3, 5) == [1, 3, 1, 1]
