from task15_6.task15_6 import unique_symbols


def test_without_unique_symbols():
    assert unique_symbols("модерна") == 7


def test_several_unique_symbols():
    assert unique_symbols("перекрытие") == 5


def test_without_symbols():
    assert unique_symbols("") == 0
