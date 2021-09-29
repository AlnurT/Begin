from task6.task6 import coin_search


def test_coin_nearby():
    assert coin_search(-3, 4, 6)


def test_coin_on_the_border():
    assert coin_search(-3, 4, 5)


def test_coin_far_away():
    assert not coin_search(-3, 4, 4.99)
