def detect_fraud(speed, pattern):
    score = 0

    if speed > 80:
        score += 40

    if pattern == "straight_line":
        score += 40

    if pattern == "no_sensor_activity":
        score += 30

    return min(score, 100)
