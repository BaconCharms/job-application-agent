def calculate_score(match_data):
    score = 0

    score += match_data["skills"] * 0.35
    score += match_data["experience"] * 0.30
    score += match_data["education"] * 0.15
    score += match_data["location"] * 0.10
    score += match_data["preferences"] * 0.10

    return round(score)