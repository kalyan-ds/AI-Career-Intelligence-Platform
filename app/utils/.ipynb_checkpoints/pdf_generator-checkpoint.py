from datetime import datetime
from reportlab.platypus import (
SimpleDocTemplate,
Paragraph,
Spacer
)
from reportlab.lib.styles import getSampleStyleSheet
def generate_pdf_report(
    technical_score,
    communication_score,
    overall_score,
    rating,
    hiring_probability,
    match_score,
    matched_skills,
    missing_skills,
    analytics
):
    pdf_file = "interview_report.pdf"
    doc = SimpleDocTemplate(
        pdf_file
    )
    styles = getSampleStyleSheet()
    content = []
    current_time = datetime.now().strftime(
        "%d-%m-%Y %H:%M"
    )
    content.append(
        Paragraph(
            "AI Career Intelligence Report",
            styles["Title"]
        )
    )
    content.append(
        Paragraph(
            f"Generated On: {current_time}",
            styles["BodyText"]
        )
    )
    content.append(
        Spacer(1, 12)
    )
    content.append(
        Spacer(1, 12)
    )
    content.append(
        Paragraph(
            "Resume Match Analysis",
            styles["Heading2"]
        )
    )
    content.append(
        Paragraph(
            f"Resume Match Score: {match_score}%",
            styles["BodyText"]
        )
    )
    content.append(
        Paragraph(
            f"Matched Skills: {', '.join(matched_skills)}",
            styles["BodyText"]
        )
    )
    content.append(
        Paragraph(
            f"Missing Skills: {', '.join(missing_skills)}",
            styles["BodyText"]
        )
    )
    content.append(
        Spacer(1, 12)
    )
    content.append(
        Paragraph(
            "Interview Results",
            styles["Heading2"]
        )
    )
    content.append(
        Paragraph(
            f"Semantic Score: {technical_score}",
            styles["BodyText"]
        )
    )
    content.append(
        Paragraph(
            f"Communication Score: {communication_score}",
            styles["BodyText"]
        )
    )
    content.append(
        Paragraph(
            f"Overall Score: {overall_score}",
            styles["BodyText"]
        )
    )
    content.append(
        Paragraph(
            f"Candidate Rating: {rating}",
            styles["BodyText"]
        )
    )
    content.append(
        Paragraph(
            f"Hiring Probability: {hiring_probability}%",
            styles["BodyText"]
        )
    )
    content.append(
        Spacer(1, 12)
    )
    content.append(
        Paragraph(
            "Interview Analytics",
            styles["Heading2"]
        )
    )
    content.append(
        Paragraph(
            f"Average Score: {analytics['average_score']}",
            styles["BodyText"]
        )
    )
    content.append(
        Paragraph(
            f"Strongest Question: {analytics['strongest_question']}",
            styles["BodyText"]
        )
    )
    content.append(
        Paragraph(
            f"Weakest Question: {analytics['weakest_question']}",
            styles["BodyText"]
        )
    )
    content.append(
        Paragraph(
            f"Best Score: {analytics['strongest_score']}",
            styles["BodyText"]
        )
    )
    doc.build(content)
    return pdf_file

