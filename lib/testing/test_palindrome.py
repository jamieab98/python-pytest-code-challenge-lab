from palindrome import longest_palindromic_substring

def test_longest_palindromic_substring():
    assert longest_palindromic_substring("racecar") == "racecar"
    assert longest_palindromic_substring("babad") in ("bab", "aba")
    assert longest_palindromic_substring("apple") == "pp"
    assert longest_palindromic_substring("dad") == "dad"
    assert longest_palindromic_substring("") == ""
    assert longest_palindromic_substring("a") == "a"
    assert longest_palindromic_substring("asdfghjklkjhgfdsa") == "asdfghjklkjhgfdsa"
    assert longest_palindromic_substring("abcdefg") in ("a", "b", "c", "d", "e", "f", "g")