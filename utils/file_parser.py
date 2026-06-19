import io
import re
import pdfplumber
import pytesseract
from PIL import Image


def extract_text_from_pdf(file_bytes):
    text_parts = []
    with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text_parts.append(page.extract_text())
    return "\n".join(text_parts)


def extract_text_from_docx(file_bytes):
    from docx import Document
    doc = Document(io.BytesIO(file_bytes))
    return "\n".join(p.text for p in doc.paragraphs)


def extract_text_from_image(file_bytes):
    image = Image.open(io.BytesIO(file_bytes))
    text = pytesseract.image_to_string(image)
    return text


def extract_text(uploaded_file):
    file_bytes = uploaded_file.read()
    uploaded_file.seek(0)
    name = uploaded_file.name.lower()

    if name.endswith(".pdf"):
        return extract_text_from_pdf(file_bytes)
    elif name.endswith(".docx"):
        return extract_text_from_docx(file_bytes)
    elif any(name.endswith(ext) for ext in (".jpeg", ".jpg", ".png")):
        return extract_text_from_image(file_bytes)
    else:
        raise ValueError(f"Unsupported file format: {name}")
