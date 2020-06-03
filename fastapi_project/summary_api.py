from fastapi import FastAPI
from pydantic import BaseModel
from text_summarizer import get_summary

app = FastAPI()

class Text(BaseModel):
    text: str

@app.post("/summarize")
def create_summary(userText: Text):
    #TODO - make this and the summarizer async
    return {"summary": get_summary(userText.text)}

@app.get("/")
def hello():
    return {"message": "Welcome to the summarizer API"}

    from fastapi import FastAPI