from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Task manager API is running"}