from fastapi import FastAPI

app = FastAPI(title="LENA")


@app.get("/")
def root():
    return {"message": "Welcome to LENA"}


@app.get("/health")
def health():
    return {"status": "ok"}
