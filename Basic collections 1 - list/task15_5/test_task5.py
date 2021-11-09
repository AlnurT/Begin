from task15_5.task5 import favorite_films

data = [
    "Крепкий орешек",
    "Назад в будущее",
    "Таксист",
    "Леон",
    "Богемская рапсодия",
    "Город грехов",
    "Мементо",
    "Отступники",
    "Деревня",
]


def test_is_favorite_film_in_the_list():
    assert favorite_films(data, "Леон")


def test_is_favorite_film_not_in_the_list():
    assert not favorite_films(data, "Форсаж")
