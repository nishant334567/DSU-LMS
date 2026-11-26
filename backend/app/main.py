from fastapi import FastAPI

from app.api.students import router as students_router

app = FastAPI(title="LENA")
app.include_router(students_router)


@app.get("/")
def root():
    return {"message": "Welcome to LENA"}


@app.get("/health")
def health():
    return {"status": "ok"}
