from task16_7.task16_7 import check_the_size_of_skates_per_person


def test_suitable_size():
    assert check_the_size_of_skates_per_person([1, 2, 3], 3) == 1


def test_no_size():
    assert check_the_size_of_skates_per_person([1, 2, 3], 4) == 0
