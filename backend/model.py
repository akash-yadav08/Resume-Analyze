def analyze_resume(text):
    required_skills = ["python", "java", "aws", "docker", "mongodb", "react"]

    text = text.lower()

    found = [s for s in required_skills if s in text]
    missing = [s for s in required_skills if s not in text]

    score = int((len(found) / len(required_skills)) * 100)

    if missing:
        suggestions = "Improve by adding: " + ", ".join(missing)
    else:
        suggestions = "Excellent resume!"

    return {
        "score": score,
        "skills_found": found,
        "missing_skills": missing,
        "suggestions": suggestions
    }