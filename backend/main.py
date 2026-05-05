from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from resume_parser import extract_text
from model import analyze_resume

# 👉 Docs enable kiye (important fix)
app = FastAPI(
    title="Resume Analyzer API",
    description="API for analyzing resumes",
    version="1.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Allow frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint
@app.get("/")
def home():
    return {"message": "Resume Analyzer API Running 🚀"}

# Analyze endpoint
@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    content = await file.read()
    text = extract_text(content)
    result = analyze_resume(text)
    return result