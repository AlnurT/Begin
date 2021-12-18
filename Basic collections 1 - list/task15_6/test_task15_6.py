from task15_6.task15_6 import coun_unique_symbols_in


def test_without_unique_symbols():
    assert coun_unique_symbols_in("модерна") == 7


def test_several_unique_symbols():
    assert coun_unique_symbols_in("перекрытие") == 5


def test_without_symbols():
    assert coun_unique_symbols_in("") == 0
