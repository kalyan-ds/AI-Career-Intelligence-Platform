from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet

from datetime import datetime

def generate_certificate(
    score,
    rating
):

    pdf_file = (
        "Interview_Certificate.pdf"
    )

    doc = SimpleDocTemplate(
        pdf_file,
        pagesize=letter
    )

    styles = getSampleStyleSheet()

    content = []

    content.append(

        Paragraph(

            "CERTIFICATE OF COMPLETION",

            styles["Title"]

        )

    )

    content.append(
        Spacer(1, 20)
    )

    content.append(

        Paragraph(

            "AI Career Intelligence Platform",

            styles["Heading2"]

        )

    )

    content.append(
        Spacer(1, 20)
    )

    content.append(

        Paragraph(

            "Awarded for Successfully Completing the AI Interview Assessment",

            styles["BodyText"]

        )

    )

    content.append(
        Spacer(1, 20)
    )

    content.append(

        Paragraph(

            f"Overall Score: {score:.1f}%",

            styles["Heading2"]

        )

    )

    content.append(

        Paragraph(

            f"Rating: {rating}",

            styles["Heading2"]

        )

    )

    content.append(
        Spacer(1, 20)
    )

    current_date = datetime.now().strftime(
        "%d-%m-%Y"
    )

    content.append(

        Paragraph(

            f"Date: {current_date}",

            styles["BodyText"]

        )

    )

    doc.build(
        content
    )

    return pdf_file
