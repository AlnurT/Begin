from task15_4.task4 import video_cards_selection


def test_list_without_best_video_cards():
    assert video_cards_selection([3070, 2060, 3090, 3070, 3090]) == [3070, 2060, 3070]


def test_list_without_all_video_cards():
    assert video_cards_selection([3090, 3090]) == []
