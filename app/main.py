from fastapi import FastAPI
from app.api.auth import router as auth_router

app = FastAPI(
    title="Job Application Tracker API",
    description="Track job applications, interviews, and follow-ups",
    version="0.1.0",
)

app.include_router(auth_router)

@app.get("/health", tags=["Health"])
def health_check() -> dict[str, str]:
    return {"status": "OK"}