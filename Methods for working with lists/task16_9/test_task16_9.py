from collections import defaultdict

from task16_9.task16_9 import calculate_debt


def test_calculate_debt():
    assert calculate_debt(defaultdict(int), 1, 2, 100) == {1: 100, 2: -100}
