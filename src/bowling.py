def _frame_score(frame: str) -> tuple[int, ...]:
    frame = frame.replace("-", "0")
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
        if i > 9:
            break
        if frame.endswith("/"):  # spare
            total_score += 10 + _frame_score(frames[i + 1])[0]
        else:
            total_score += sum(_frame_score(frame))
    return total_score
