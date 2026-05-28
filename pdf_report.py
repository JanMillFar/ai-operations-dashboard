from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter


def generar_pdf(informe_ia):

    pdf = SimpleDocTemplate(
        "executive_report.pdf",
        pagesize=letter
    )

    styles = getSampleStyleSheet()

    elementos = []

    titulo = Paragraph(
        "AI Operations Executive Report",
        styles['Title']
    )

    elementos.append(titulo)

    elementos.append(Spacer(1, 20))

    contenido = Paragraph(
        informe_ia.replace("\n", "<br/>"),
        styles['BodyText']
    )

    elementos.append(contenido)

    pdf.build(elementos)

    return "executive_report.pdf"