import pytest
from task15_2.task2 import team_selection


@pytest.mark.parametrize(
    ("all_names", "team"),
    [
        (
            ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"],
            ["Борис", "Гоша", "Евгений", "Захар"],
        ),
        (["Артемий"], []),
        ([], []),
    ],
)
def test_every_second_team_member(all_names, team):
    assert team_selection(all_names) == team
