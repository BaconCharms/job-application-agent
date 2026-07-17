from agent.agent import ask_agent
import re
import ast



def qualify_job(job_info, analysis):

    prompt = f"""
You are a job application decision agent.

Evaluate whether this job is worth applying to.

Return ONLY a valid Python dictionary.

Format:

{{
    "decision": "APPROVE",
    "match_score": 0,
    "reason": ""
}}

Rules:

APPROVE:
- Match score >= 70
- Job aligns with accounting/finance career goals
- Location is reasonable

REJECT:
- Match score < 70
- Not related to accounting/finance
- Clearly incompatible requirements


JOB INFORMATION:

{job_info}


RESUME ANALYSIS:

{analysis}

"""


    response = ask_agent(prompt)



    # Remove markdown formatting if AI adds it

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



    # Extract dictionary

    start = response.find("{")
    end = response.rfind("}") + 1


    if start == -1 or end == 0:

        raise ValueError(
            "Could not parse qualification response:\n"
            + response
        )


    response = response[start:end]


    decision = ast.literal_eval(
        response
    )


    return decision