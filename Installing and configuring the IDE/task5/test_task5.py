from task5.task5 import least_divisor


def test_least_divisor_for_compound_odd_numbers():
    assert least_divisor(15) == 3


def test_least_divisor_for_compound_even_numbers():
    assert least_divisor(16) == 2


def test_least_divisor_for_simple_numbers():
    assert least_divisor(17) == 17
