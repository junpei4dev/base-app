from fastapi import FastAPI

from . import schemas

app = FastAPI()


@app.get("/health-check", response_model=schemas.HealthCheck)
def health_check() -> schemas.HealthCheck:
    return schemas.HealthCheck(status="ok")
