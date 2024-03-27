# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/api/python")
# def hello_world():
#     return {"message": "Hello World"}




# import uvicorn

from fastapi import FastAPI, Request, Header
from fastapi.middleware.cors import CORSMiddleware
from .ai import Ai

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api")
async def read_root():
    return {"message": "Server Running"}


@app.post("/api")
async def gemini(request: Request, key: str = Header(None)):
    qna_dict = await request.json()
    qna_str = str(qna_dict)
    res = Ai.gemini(qna_str, key)
    return res

