from dotenv import load_dotenv

from openai import OpenAI
from prompt_template import build_prompt
import os

load_dotenv()


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_question(domain, difficulty, previous_answer, language):

    prompt = build_prompt(domain, difficulty, previous_answer, language)

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    question = response.choices[0].message.content

    return question

print(os.getenv("OPENAI_API_KEY"))