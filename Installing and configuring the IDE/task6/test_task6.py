from task6.task6 import is_coin_in_circle


def test_coin_nearby():
    assert is_coin_in_circle(-3, 4, 6)


def test_coin_on_the_border():
    assert is_coin_in_circle(-3, 4, 5)


def test_coin_far_away():
    assert not is_coin_in_circle(-3, 4, 4.99)
