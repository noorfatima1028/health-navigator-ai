from app.services.symptom_assessment import assess_symptoms


response = assess_symptoms(
    age=25,
    sex="Female",
    symptoms=["headache", "fever"],
    duration="2 days",
)

print(response)