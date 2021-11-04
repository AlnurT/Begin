from task15_7.task15_7 import number_of_new_container, sorted_list_weight


def test_sorted_list_weight():
    assert sorted_list_weight([168, 170, 150, 199, 170]) == [199, 170, 170, 168, 150]


def test_number_of_new_container():
    assert number_of_new_container([199, 170, 170, 168, 150], 170) == 4


def test_if_new_container_is_first():
    assert number_of_new_container([199, 170, 170, 168, 150], 200) == 1


def test_if_new_container_is_last():
    assert number_of_new_container([199, 170, 170, 168, 150], 150) == 6
