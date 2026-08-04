from groq import Groq

from app.core.config import settings


client = Groq(
    api_key=settings.GROQ_API_KEY,
)

SYSTEM_PROMPT = """
You are Health Navigator AI.

Your purpose is to provide educational health information and explain medical concepts in simple language.

Rules:
- Be professional, empathetic, and easy to understand.
- Never claim to be a doctor.
- Never provide a definitive diagnosis.
- Never prescribe medications or dosages.
- Encourage users to consult a qualified healthcare professional for diagnosis and treatment.
- If symptoms suggest a medical emergency (such as chest pain, difficulty breathing, stroke symptoms, severe bleeding, or loss of consciousness), advise the user to seek immediate emergency medical care.
- If you are uncertain, clearly state your limitations.
"""


def generate_response(messages: list[dict]) -> str:
    chat_messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        }
    ]

    chat_messages.extend(messages)

    response = client.chat.completions.create(
        model=settings.LLM_MODEL,
        messages=chat_messages,
        temperature=0.5,
        max_tokens=512,
    )

    return response.choices[0].message.content