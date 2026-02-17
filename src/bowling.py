def _frame_score(frame: str) -> tuple[int, ...]:
    frame = frame.replace("-", "0")
    if frame == "X":
        return 10,
    first = int(frame[0])
    if frame.endswith("/"):
        second = 10 - first
    elif len(frame) == 1:
        second = 0
    else:
        second = int(frame[1])
    return first, second


def score(line: str) -> int:
    total_score = 0
    frames = line.split()
    for i, frame in enumerate(frames):
        if i >= 10:
            break
        if frame.endswith("/"):  # spare
            bonus_roll = _frame_score(frames[i + 1])
            total_score += 10 + bonus_roll[0]
        elif frame == "X":  # strike
            bonus_roll_1 = _frame_score(frames[i + 1])
            bonus_roll_2 = _frame_score(frames[i + 2])[0] \
                if len(bonus_roll_1) == 1 else bonus_roll_1[1]
            total_score += 10 + bonus_roll_1[0] + bonus_roll_2
        else:
            total_score += sum(_frame_score(frame))
    return total_score
