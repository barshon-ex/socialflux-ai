from fastapi import FastAPI

app = FastAPI(
    title="SocialFlux AI",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "project": "SocialFlux AI",
        "status": "Running"
    }

@app.get("/health")
def health():
    return {
        "status": "ok"
    }
