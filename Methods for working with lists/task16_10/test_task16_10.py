from task16_10.task16_10 import assign_numbers_for_list_symmetry


def test_symmetry_not_listed():
    assert assign_numbers_for_list_symmetry([1, 2, 3, 4], []) == (3, [3, 2, 1])


def test_partial_symmetry_in_list():
    assert assign_numbers_for_list_symmetry([1, 3, 2, 2], []) == (2, [3, 1])
