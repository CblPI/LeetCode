import pytest

from tasks.word_pattern import Solution


@pytest.mark.parametrize(
    "string, pattern, result", [
        (
            "dog cat cat dog",
            "abba",
            True
        ),
        (
            "dog cat pogchamp dog cat",
            "abcab",
            True
        ),
        (
            "dog cat pogchamp cat",
            "abab",
            False
        ),
        (
            "dog cat pogchamp cat",
            "abab",
            False
        ),
        (
            "dog cat pogchamp",
            "abab",
            False
        ),
        (
            "dog dog dog dog",
            "abab",
            False
        )
    ]
)
def test_word_pattern(string, pattern, result):
    assert Solution.wordPattern(pattern, string) is result
