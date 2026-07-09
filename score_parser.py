import re


def extract_match_score(analysis):

    match = re.search(
        r"(\d{1,3})/100",
        analysis
    )

    if match:
        return int(match.group(1))

    return 0