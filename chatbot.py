from transformers import pipeline
from prompts import SYSTEM_PROMPT, SYMPTOM_PROMPTS, EMERGENCY_KEYWORDS, EMERGENCY_RESPONSE

MODEL_NAME = "google/flan-t5-small"

import streamlit as st

@st.cache_resource
def load_model():
    return pipeline(
        "text2text-generation",
        model=MODEL_NAME,
        torch_dtype="auto",
        device_map="cpu"
    )

pipe = load_model()


def check_emergency(user_text):
    text_lower = user_text.lower()
    for keyword in EMERGENCY_KEYWORDS:
        if keyword in text_lower:
            return True
    return False


def generate_response(user_prompt):
    full_prompt = SYSTEM_PROMPT + "\n\n" + user_prompt
    outputs = pipe(full_prompt, max_new_tokens=350)
    return outputs[0]["generated_text"].strip()


def get_response_for_symptom(symptom_key):
    if symptom_key not in SYMPTOM_PROMPTS:
        return "Invalid selection. Please choose a valid option."

    user_prompt = SYMPTOM_PROMPTS[symptom_key] + " Do not repeat these instructions back. Directly give the advice."
    response = generate_response(user_prompt)

    # Remove any leaked instruction text if model repeats it
    if "Rules you MUST follow" in response:
        parts = response.split("Rules you MUST follow")
        response = parts[-1]
        # Clean up leftover numbered rules if present
        if "5." in response:
            response = response.split("5.", 1)[-1]
            if '"' in response:
                response = response.split('"', 2)[-1]

    return response.strip()


def get_response_for_freetext(user_text):
    if check_emergency(user_text):
        return EMERGENCY_RESPONSE

    return generate_response(f"The user says: '{user_text}'. Respond following the rules.")