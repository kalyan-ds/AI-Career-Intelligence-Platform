import fitz
from docx import Document

def extract_text(file):

    filename = file.name.lower()

    if filename.endswith(".pdf"):

        pdf = fitz.open(
            stream=file.read(),
            filetype="pdf"
        )

        text = ""

        for page in pdf:
            text += page.get_text()

        return text

    elif filename.endswith(".docx"):

        doc = Document(file)

        text = "\n".join(
            para.text
            for para in doc.paragraphs
        )

        return text

    elif filename.endswith(".txt"):

        return file.read().decode()

    return ""