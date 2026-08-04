from groq import Groq
from app.core.config import settings

client = Groq(api_key=settings.GROQ_API_KEY)


def generate_response(messages: list) -> str:
    response = client.chat.completions.create(
        model=settings.LLM_MODEL,
        messages=messages,
        temperature=0.5,
        max_tokens=512,
    )

    return response.choices[0].message.content