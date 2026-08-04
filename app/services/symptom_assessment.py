from app.services.llm_service import generate_response


def assess_symptoms(
    age: int,
    sex: str,
    symptoms: list[str],
    duration: str,
) -> str:

    prompt = f"""
Patient Information

Age: {age}
Sex: {sex}

Symptoms:
{", ".join(symptoms)}

Duration:
{duration}

Provide:

1. A brief educational summary.
2. Possible explanations (not a diagnosis).
3. Red flag symptoms to watch for.
4. General self-care advice.
5. When the patient should seek medical care.

Do not diagnose diseases.
Do not prescribe medications.
"""

    return generate_response(
        [
            {
                "role": "user",
                "content": prompt,
            }
        ]
    )