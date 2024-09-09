import pytest

from tasks.check_if_n_and_its_double_exist import Solution


@pytest.mark.parametrize(
    "array, result", [
        ([10, 2, 5, 3], True),
        ([3, 1, 7, 11], False),
        ([5, 1, 5, 5], False)
    ]
)
def test_if_double_exist(array, result):
    assert Solution.checkIfExist(array) is result