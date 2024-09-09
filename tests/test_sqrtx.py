import pytest

from tasks.sqrtx import Solution


@pytest.mark.parametrize(
    "item, result", [
        (4, 2),
        (256, 16),
        (4096, 64),
        (1024, 32),
    ]
)
def test_sqrtx(item, result):
    assert Solution.mySqrt(item) == result