SYSTEM_PROMPT = """You are a helpful first-aid and health awareness assistant for rural communities.
Rules you MUST follow:
1. Give only general, safe, non-prescriptive advice (home remedies, hygiene, when to rest, when to drink fluids, etc.)
2. NEVER prescribe medicines, dosages, or specific drug names.
3. NEVER attempt to diagnose a specific disease.
4. Keep your answer short (3-5 sentences), simple, and in plain language.
5. Always end with: "This is general advice only. Please visit your nearest health worker or doctor if symptoms continue or worsen."
"""

SYMPTOM_PROMPTS = {
    "1": "The user has reported: Fever. Give simple home-care advice for managing a mild fever.",
    "2": "The user has reported: Cough and cold. Give simple home-care advice for managing cough/cold symptoms.",
    "3": "The user has reported: Stomach pain or upset stomach. Give simple home-care advice.",
    "4": "The user has reported: Minor cuts, wounds, or burns. Give simple first-aid advice.",
    "5": "The user has reported: Headache or body pain. Give simple home-care advice.",
    "6": "The user has reported: General hygiene and nutrition question. Give simple practical advice on hygiene and healthy eating."
}

EMERGENCY_KEYWORDS = [
    "chest pain", "difficulty breathing", "unconscious", "severe bleeding",
    "not breathing", "seizure", "fainted", "snake bite", "poisoning",
    "heart attack", "stroke", "accident"
]

EMERGENCY_RESPONSE = (
    "This sounds like a medical EMERGENCY.\n"
    "Please go to the nearest hospital IMMEDIATELY or call emergency services / ASHA worker.\n"
    "Do not wait. Get help now."
)