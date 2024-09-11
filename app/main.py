from fastapi import FastAPI
from schemas.schema import Payload
from crud.crud import run_formula

app = FastAPI()


@app.post("/api/execute-formula")
async def execute_formula(payload: Payload):
    return run_formula(payload)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
