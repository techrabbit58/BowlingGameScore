def score(frames: str) -> int:
    total_score = 0
    for c in frames:
        if c not in "-\n\t\r ":
            total_score += int(c)
    return total_score
