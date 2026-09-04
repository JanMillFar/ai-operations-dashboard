from groq import Groq
from groq_config import get_groq_model, get_groq_setting, is_groq_enabled

# FUNCIÓN IA
def generar_informe_ia(incidencias_texto):
    if not is_groq_enabled():
        raise RuntimeError("Groq is disabled to prevent API charges.")

    api_key = get_groq_setting("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("GROQ_API_KEY is not configured.")

    client = Groq(api_key=api_key)

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
        model=get_groq_model(),
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
