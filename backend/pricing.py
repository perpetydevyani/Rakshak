def calculate_premium(risk_score):
    if risk_score < 30:
        return 15
    elif risk_score < 70:
        return 25
    else:
        return 40
