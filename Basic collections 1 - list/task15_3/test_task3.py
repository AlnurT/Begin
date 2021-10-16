from task15_3.task3 import cell_selection


def test_cell_with_low_efficiency():
    assert cell_selection(5, [3, 0, 6, 2, 10]) == "0 2 "
