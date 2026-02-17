def _deliveries(frame: str) -> tuple[int, ...]:
    frame = frame.replace("-", "0")
    first = int(frame[0])
    second = 10 - first if frame.endswith("/") else int(frame[1])
    return first, second


def score(line: str) -> int:
    total_score = 0
    frames = line.split()
    for i, frame in enumerate(frames):
        if frame[-1] == "/":  # spare
            total_score += 10 + _deliveries(frames[i + 1])[0]
        else:
            total_score += sum(_deliveries(frame))
    return total_score
