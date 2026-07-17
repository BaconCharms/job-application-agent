from config.settings import MIN_MATCH_SCORE

def should_apply(score):
    return score >= MIN_MATCH_SCORE