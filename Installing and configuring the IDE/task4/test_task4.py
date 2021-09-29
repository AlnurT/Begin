from decimal import Decimal

from task4.task4 import reverse_number


def test_reverse_number():
    assert reverse_number("1256.874") == Decimal("6521.478")
