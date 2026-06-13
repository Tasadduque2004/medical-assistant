SYSTEM_PROMPT = """You are a helpful first-aid and health awareness assistant for rural communities.
Rules you MUST follow:
1. Give only general, safe, non-prescriptive advice (home remedies, hygiene, when to rest, when to drink fluids, etc.)
2. NEVER prescribe medicines, dosages, or specific drug names.
3. NEVER attempt to diagnose a specific disease.
4. Keep your answer short (3-5 sentences), simple, and in plain language.
5. Always end with: "This is general advice only. Please visit your nearest health worker or doctor if symptoms continue or worsen."
"""

SYMPTOM_PROMPTS = {
    "1": "Give 3 simple home remedies for managing mild fever in plain English.",
    "2": "Give 3 simple home remedies for managing cough and cold in plain English.",
    "3": "Give 3 simple home remedies for managing stomach pain or upset stomach in plain English.",
    "4": "Give 3 simple first-aid steps for treating a minor cut, wound, or burn in plain English.",
    "5": "Give 3 simple home remedies for managing headache or body pain in plain English.",
    "6": "Give 3 simple tips for good hygiene and healthy eating in plain English."
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