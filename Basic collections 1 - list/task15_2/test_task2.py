from task15_2.task2 import team_selection


def test_every_second_team_member():
    assert team_selection(
        ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]
    ) == ["Борис", "Гоша", "Евгений", "Захар"]
