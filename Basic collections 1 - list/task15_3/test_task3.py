from task15_3.task3 import cell_selection


def test_cells_with_low_efficiency():
    assert cell_selection([3, 0, 6, 2, 10]) == "0 2"


def test_cells_without_low_efficiency():
    assert cell_selection([3, 2, 6, 5, 10]) == ""
