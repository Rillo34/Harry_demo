from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:3000",
    "http://localhost:8081",
    "http://localhost:8001",
    "http://127.0.0.1:8081",
    "http://127.0.0.1:8005",
    "http://46.62.140.27:8091",
    "http://localhost:8091",
    "http://127.0.0.1:8091",
    "http://localhost:8092",
    "http://127.0.0.1:8092"

]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Backend demo is running"}

@app.get("/api/ping")
def ping():
    return {"status": "ok", "message": "pong from backend"}

@app.post("/api/echo")
def echo(data: dict):
    return {"you_sent": data}
