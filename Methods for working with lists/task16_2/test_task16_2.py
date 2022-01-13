from task16_2.task16_2 import create_list


def test_create_list():
    assert create_list(1, 11, 2) == [1, 3, 5, 7, 9, 11]
