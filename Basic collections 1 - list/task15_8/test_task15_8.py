from task15_8.task15_8 import shift_of_elements_in_list


def test_positive_shift_of_elements():
    assert shift_of_elements_in_list([1, 4, -3, 0, 10], 3) == [-3, 0, 10, 1, 4]


def test_negative_shift_of_elements():
    assert shift_of_elements_in_list([1, 4, -3, 0, 10], -3) == [0, 10, 1, 4, -3]


def test_zero_shift_of_elements():
    assert shift_of_elements_in_list([1, 4, -3, 0, 10], 0) == [1, 4, -3, 0, 10]
