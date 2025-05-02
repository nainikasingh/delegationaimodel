from fastapi import APIRouter, Query
from app.utils import load_user_role, load_user_name
from app.qna_questions import BOSS_QUESTIONS, DELEGATOR_QUESTIONS, DELEGATEE_QUESTIONS

router = APIRouter()

@router.post("/generate_qna/")
def generate_qna(user_id: str = Query(..., alias="_id")):
    role = load_user_role(user_id)
    username = load_user_name(user_id)

    if role is None or username is None:
        return {"error": "User not found"}

    questions = []

    if role.lower() == "boss":
        questions.extend(BOSS_QUESTIONS + DELEGATOR_QUESTIONS + DELEGATEE_QUESTIONS)
    elif role.lower() == "delegator":
        questions.extend(DELEGATOR_QUESTIONS + DELEGATEE_QUESTIONS)
    elif role.lower() == "delegatee":
        questions.extend(DELEGATEE_QUESTIONS)
    else:
        return {"error": "Invalid user role"}

    return {
        "user_id": user_id,
        "username": username,
        "role": role,
        "questions": questions
    }
