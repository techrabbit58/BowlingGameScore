import pytest

import bowling


@pytest.mark.parametrize("actual_line, expected_score", [
    ("-- -- -- -- -- -- -- -- -- --", 0),
    ("12 12 12 12 12 12 12 12 12 12", 30),
    ("9- 9- 9- 9- 9- 9- 9- 9- 9- 9-", 90),
    ("6/ 8- -- -- -- -- -- -- -- --", 26),
    ("5/ 5/ 1- 1- 1- 1- 1- 1- 1- 1-", 34),
    ("5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 54", 144),
    ("5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5", 150),
    ("-- -- -- -- -- -- -- -- -- 5/ 5", 15),
    ("X 81 -- -- -- -- -- -- -- --", 28),
    ("X 8/ 12 -- -- -- -- -- -- --", 34),
    ("X X X X X X X X X 12", 247),
    ("X 5/ X 5/ X 5/ X 5/ X 5/ X", 200),
    ("5/ X 5/ X 5/ X 5/ X 5/ X 5/", 200),
    ("X X X X X X X X X X X X", 300),
])
def test_score(actual_line, expected_score):
    assert bowling.score(actual_line) == expected_score
