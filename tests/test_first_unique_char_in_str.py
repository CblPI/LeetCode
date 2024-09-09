import pytest

from tasks.first_unique_character_in_a_string import Solution


@pytest.mark.parametrize(
    "char, index", [
        ("aboba", 2),
        ("test", 1),
        ("hello", 0),
        ("AAAAA", -1)
    ]
)
def test_first_unic_char(char, index):
    assert Solution.firstUniqChar(char) == index
