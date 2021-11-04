from task15_9.task15_9 import word_is_palindrome


def test_is_word_palindrome():
    assert word_is_palindrome("мадам")


def test_is_word_not_palindrome():
    assert not word_is_palindrome("модем")
