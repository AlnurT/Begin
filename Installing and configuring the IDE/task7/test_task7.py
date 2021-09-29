from task7.task7 import special_years


def test_years_with_3_identical_digits():
    assert special_years(1900, 2100) == "1911\n1999\n2000\n2022\n"


def test_years_without_identical_digits():
    assert special_years(1912, 1998) == ""
