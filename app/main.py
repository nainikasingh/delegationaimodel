from fastapi import FastAPI
from app.api import router

app = FastAPI(
    title="Delegation AI",
    description="Role-based Q&A Generator for Task Delegation",
    version="1.0.0"
)

app.include_router(router)
