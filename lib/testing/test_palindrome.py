import pytest
from palindrome import longest_palindromic_substring

@pytest.mark.parametrize("a, expected", [
    ("racecar", "racecar"),
    ("apple", "pp"),
    ("asdfdsa", "asdfdsa"),
    ("", ""),
    ("a", "a"),
    ("qwertyuioppoiuytrewq", "qwertyuioppoiuytrewq")
])

def test_longest_palindromic_substring(a, expected):
    assert longest_palindromic_substring(a) == expected