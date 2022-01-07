from task16_4.task16_4 import add_or_remove_guests

guests = ["Петя", "Ваня", "Саша", "Лиза", "Катя", "Талга"]


def test_add_guest():
    assert add_or_remove_guests(["Лёха"], "пришёл", "Талга") == ["Лёха", "Талга"]


def test_add_guest_if_guests_more_than_6():
    assert add_or_remove_guests(guests, "пришёл", "Лёха") == guests


def test_remove_guest():
    assert add_or_remove_guests(["Лёха", "Талга"], "ушёл", "Талга") == ["Лёха"]


def test_remove_guest_if_guests_are_none():
    assert add_or_remove_guests([], "ушёл", "Лёха") == []
