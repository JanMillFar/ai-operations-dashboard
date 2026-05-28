import os
from groq import Groq
from dotenv import load_dotenv

# CARGAR VARIABLES DE ENTORNO
load_dotenv()

# CLIENTE GROQ
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# FUNCIÓN IA
def generar_informe_ia(incidencias_texto):

    prompt = f"""
    Analyze the following operational incidents and generate:

    1. Executive summary
    2. Operational risks
    3. Recommended actions
    4. Priority level

    Incidents:
    {incidencias_texto}
    """

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.4,
        max_tokens=500
    )

    return completion.choices[0].message.content