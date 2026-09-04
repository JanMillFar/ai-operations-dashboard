from google import genai

from gemini_config import (
    get_gemini_free_model,
    get_gemini_setting,
    is_gemini_free_enabled,
)

# FUNCIÓN IA
def generar_informe_ia(incidencias_texto):
    if not is_gemini_free_enabled():
        raise RuntimeError("Gemini Free is disabled to prevent unintended API charges.")

    api_key = get_gemini_setting("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not configured.")

    client = genai.Client(api_key=api_key)

    prompt = f"""
    Analyze the following operational incidents and generate:

    1. Executive summary
    2. Operational risks
    3. Recommended actions
    4. Priority level

    Incidents:
    {incidencias_texto}
    """

    interaction = client.interactions.create(
        model=get_gemini_free_model(),
        input=prompt,
        store=False,
    )

    return interaction.output_text
