from task15_9.task15_9 import is_word_palindrome


def test_is_word_palindrome():
    assert is_word_palindrome("мадам")


def test_is_word_not_palindrome():
    assert not is_word_palindrome("модем")
