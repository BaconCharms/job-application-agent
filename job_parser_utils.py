import ast
import re


def parse_job_info(response):

    # Remove markdown code blocks
    response = re.sub(
        r"```(?:python|json)?",
        "",
        response
    )

    response = response.replace(
        "```",
        ""
    )

    response = response.strip()


    # Extract only the dictionary portion
    start = response.find("{")
    end = response.rfind("}") + 1

    if start == -1 or end == 0:
        raise ValueError(
            "Could not find dictionary in AI response:\n"
            + response
        )

    response = response[start:end]


    job_info = ast.literal_eval(response)

    return job_info