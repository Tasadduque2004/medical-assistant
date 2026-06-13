SYSTEM_PROMPT = """You are a helpful first-aid and health awareness assistant for rural communities.
Rules you MUST follow:
1. Give only general, safe, non-prescriptive advice (home remedies, hygiene, when to rest, when to drink fluids, etc.)
2. NEVER prescribe medicines, dosages, or specific drug names.
3. NEVER attempt to diagnose a specific disease.
4. Keep your answer short (3-5 sentences), simple, and in plain language.
5. Always end with: "This is general advice only. Please visit your nearest health worker or doctor if symptoms continue or worsen."
"""

SYMPTOM_PROMPTS = {
    "1": "List 5 home remedies and precautions for managing mild fever. Include rest, fluids, food, when to use a wet cloth, and warning signs to watch for.",
    "2": "List 5 home remedies and precautions for managing cough and cold. Include drinks, steam, food, rest tips, and warning signs to watch for.",
    "3": "List 5 home remedies and precautions for managing stomach pain or upset stomach. Include diet changes, hydration, rest, and warning signs to watch for.",
    "4": "List 5 first-aid steps for treating a minor cut, wound, or burn at home, including cleaning, bandaging, and signs of infection to watch for.",
    "5": "List 5 home remedies and precautions for managing headache or body pain, including rest, hydration, posture, and warning signs to watch for.",
    "6": "List 5 simple daily habits for good hygiene and healthy eating in rural households."
}
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