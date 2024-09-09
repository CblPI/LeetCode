import pytest

from tasks.first_bad_version import Solution, set_target

@pytest.mark.parametrize(
    "target", [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    ]
)
def test_firs_bad_version(target):
    set_target(target)
    Solution.firstBadVersion(target)