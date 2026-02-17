import pytest

import bowling


@pytest.mark.parametrize("actual_line, expected_score", [
    ("-- -- -- -- -- -- -- -- -- --", 0),
    ("12 12 12 12 12 12 12 12 12 12", 30),
    ("9- 9- 9- 9- 9- 9- 9- 9- 9- 9-", 90),
])
def test_score(actual_line, expected_score):
    assert bowling.score(actual_line) == expected_score
