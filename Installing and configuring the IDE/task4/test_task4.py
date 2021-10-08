from task4.task4 import assembly_number, reverse_number


def test_reverse_int_number():
    assert reverse_number("1256.874", 0) == "6521"


def test_reverse_fractional_number():
    assert reverse_number("1256.874", 1) == "478"


def test_assembly_number():
    assert assembly_number("1256.874") == 6521.478
