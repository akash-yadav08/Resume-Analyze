from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from resume_parser import extract_text
from model import analyze_resume

app = FastAPI()

# Allow frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Resume Analyzer API Running 🚀"}

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    content = await file.read()
    text = extract_text(content)
    result = analyze_resume(text)
    return result