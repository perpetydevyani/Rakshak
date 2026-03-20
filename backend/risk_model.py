def predict_risk(weather, pollution):
    risk = 0

    if weather == "rain":
        risk += 40
    if weather == "flood":
        risk += 60
    if pollution == "high":
        risk += 20

    return min(risk, 100)
