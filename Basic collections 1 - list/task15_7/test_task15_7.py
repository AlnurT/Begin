from task15_7.task15_7 import show_number_of_new_container, sort_list_weight, is_weight_more_than_200


def test_sorted_list_weight():
    assert sort_list_weight([168, 170, 150, 199, 170]) == [199, 170, 170, 168, 150]


def test_number_of_new_container():
    assert show_number_of_new_container([199, 170, 170, 168, 150], 170) == 4


def test_if_new_container_is_first():
    assert show_number_of_new_container([199, 170, 170, 168, 150], 200) == 1


def test_if_new_container_is_last():
    assert show_number_of_new_container([199, 170, 170, 168, 150], 150) == 6


def test_is_weight_more_than_200():
    assert is_weight_more_than_200(206)


def test_is_weight_smaller_than_200():
    assert not is_weight_more_than_200(200)
