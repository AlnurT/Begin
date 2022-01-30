from task17_2.task17_2 import list_of_units_and_remainders


def test_list_of_units_and_remainders():
    assert list_of_units_and_remainders(10) == [1, 1, 1, 3, 1, 0, 1, 2, 1, 4]
