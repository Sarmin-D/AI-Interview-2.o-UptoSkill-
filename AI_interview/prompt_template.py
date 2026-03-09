def build_prompt(domain, difficulty, previous_answer, language):

    prompt = f"""
You are an AI technical interviewer.

Your task is to generate exactly ONE interview question.

Interview Context:
Domain: {domain}
Difficulty Level: {difficulty}
Previous Answer From Candidate: {previous_answer}
Language: {language}

Rules:
- Ask only ONE question.
- Do not give explanation.
- Keep the tone professional like a real interviewer.
- Make the question relevant to the domain.
- Adjust difficulty based on the given level.
- Output only the question text.

Return only the question.
"""

    return prompt