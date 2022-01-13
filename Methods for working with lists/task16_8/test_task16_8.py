from task16_8.task16_8 import show_retired_index


def test_last_retired():
    assert show_retired_index([1, 2, 3], 3, 0) == -1


def test_first_retired():
    assert show_retired_index([1, 2, 3], 6, 1) == 0


def test_retired_in_the_middle():
    assert show_retired_index([1, 2, 3], 5, 0) == 1
