from fastapi import FastAPI
from pydantic import BaseModel
from question_generator import generate_question

app = FastAPI()


class QuestionRequest(BaseModel):
    domain: str
    difficulty: str
    previous_answer: str
    language: str


@app.get("/")
def home():
    return {"message": "AI Interviewer Running"}


@app.post("/generate-question")
def create_question(data: QuestionRequest):

    question = generate_question(
        data.domain,
        data.difficulty,
        data.previous_answer,
        data.language
    )

    return {
        "generated_question": question
    }

