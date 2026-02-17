import bowling


def test_all_misses():
    frames = "-- -- -- -- -- -- -- -- -- --"
    assert bowling.score(frames) == 0
