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


def test_0_of_details_in_the_shop():
    assert find_the_number_of_details_and_their_cost(shop, "руль") == (0, 0)


def test_1_of_details_in_the_shop():
    assert find_the_number_of_details_and_their_cost(shop, "рама") == (1, 12000)


def test_3_of_details_in_the_shop():
    assert find_the_number_of_details_and_their_cost(shop, "седло") == (3, 4500)
