from openai import OpenAI
from dotenv import load_dotenv
import os

# Carregar variables entorn
load_dotenv()

# Client OpenAI
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def generar_informe_ia(incidencias_texto):

    prompt = f"""
    Eres un analista senior de logística y operaciones.

    Analiza estas incidencias:

    {incidencias_texto}

    Genera:
    - resumen ejecutivo
    - nivel de riesgo
    - recomendaciones
    - acciones prioritarias

    Responde de forma profesional.
    """

    try:

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": "Eres experto en operaciones."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:

        return f"ERROR OPENAI API: {e}"