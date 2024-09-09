import pytest

from tasks.anagram import Solution

@pytest.mark.parametrize(
    "first, second, result", [
        ('магаран', 'нагарам', True),
        ('мара', 'арам', True),
        ('momo', 'mmoo', True),
        ('qwert', 'ytrewq', False),
        ('aa', 'a', False)
    ]
)
def test_anagram(first, second, result):
    assert Solution.isAnagram(first, second) is result