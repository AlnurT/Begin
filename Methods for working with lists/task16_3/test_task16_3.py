import pytest
from task16_3.task16_3 import find_the_number_of_details_and_their_cost

shop = [
    ["каретка", 1200],
    ["шатун", 1000],
    ["седло", 300],
    ["педаль", 100],
    ["седло", 1500],
    ["рама", 12000],
    ["обод", 2000],
    ["шатун", 200],
    ["седло", 2700],
]


@pytest.mark.parametrize(
    ("detail", "number_of_details_and_price"),
    [("руль", (0, 0)), ("рама", (1, 12000)), ("седло", (3, 4500))],
)
def test_details_in_the_shop(detail, number_of_details_and_price):
    assert (
        find_the_number_of_details_and_their_cost(shop, detail)
        == number_of_details_and_price
    )
