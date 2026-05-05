import io
from pdfminer.high_level import extract_text as pdf_extract

def extract_text(file_bytes):
    try:
        return pdf_extract(io.BytesIO(file_bytes))
    except Exception as e:
        return ""