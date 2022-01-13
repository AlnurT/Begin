from task16_9.task16_9 import calculate_debt

dict_of_debt = dict.fromkeys(range(1, 4), 0)


def test_calculate_debt():
    assert calculate_debt(dict_of_debt, 1, 2, 100) == {1: 100, 2: -100, 3: 0}
