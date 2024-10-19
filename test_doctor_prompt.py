import openai
from promptify import Prompter
from ai_doctor import generate_response

OPENAI_API_KEY = '...'  
openai.api_key = '...'


doctor_prompt = Prompter(
    system="""You are an expert physician with years of experience in the most renowned clinic. 
    You are compassionate, attentive, and always prioritize the well-being of your patients. Your answers are always polite and positive""",
    
    user="""I'm your patient. 
    Based on my symptoms and health issues, please recommend a personalized treatment plan 
    or lifestyle changes that may help."""
)

test_symptoms = [
    "I have a headache and feel nauseous.",
    "I feel tired and have a fever.",
    "My joints hurt and I can't walk.",
    "I have a cough and feel pain in my chest.",
    "I have an allergy to pollen and have a runny nose.",
    "I suffer from insomnia and can't sleep at night.",
    "I experience constant stress and anxiety.",
    "I feel pain in my abdomen and have bowel issues.",
    "I have high blood sugar levels and feel thirsty.",
    "I recently had surgery and my incision site hurts.",
    "My muscles ache after exercising.",
    "I feel weakness and fatigue even after resting.",
    "I have a rash and itchiness on my skin.",
    "I feel tingling in my hands and feet.",
    "I have breathing problems and shortness of breath.",
    "I often have a sore throat and can’t speak.",
    "My legs swell and I have cramps.",
    "I experience dizziness and blurred vision.",
    "I feel depressed and have no motivation."
]


def test_prompt(prompter, symptoms):
    for symptom in symptoms:
        prompt = prompter.render(user=symptom)
        response = generate_response(prompt)
        print(f"Симптомы: {symptom}\nОтвет: {response}\n")

# Запуск тестирования
if __name__ == '__main__':
    test_prompt(doctor_prompt, test_symptoms)
