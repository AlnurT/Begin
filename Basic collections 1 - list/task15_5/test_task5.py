from task15_5.task5 import is_film_on_list

data = {
    "Крепкий орешек",
    "Назад в будущее",
    "Таксист",
    "Леон",
    "Богемская рапсодия",
    "Город грехов",
    "Мементо",
    "Отступники",
    "Деревня",
}


def test_favorite_films_is_in_the_list():
    assert is_film_on_list(data, "Леон")


def test_favorite_films_isnt_in_the_list():
    assert not is_film_on_list(data, "Форсаж")
