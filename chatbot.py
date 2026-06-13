import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from prompts import SYSTEM_PROMPT, SYMPTOM_PROMPTS, EMERGENCY_KEYWORDS, EMERGENCY_RESPONSE

MODEL_NAME = "google/flan-t5-small"


@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
    return tokenizer, model


tokenizer, model = load_model()


def check_emergency(user_text):
    text_lower = user_text.lower()
    for keyword in EMERGENCY_KEYWORDS:
        if keyword in text_lower:
            return True
    return False


def generate_response(user_prompt):
    full_prompt = SYSTEM_PROMPT + "\n\n" + user_prompt
    inputs = tokenizer(full_prompt, return_tensors="pt", truncation=True, max_length=512)
    outputs = model.generate(**inputs, max_new_tokens=350)
    return tokenizer.decode(outputs[0], skip_special_tokens=True).strip()


def get_response_for_symptom(symptom_key):
    if symptom_key not in SYMPTOM_PROMPTS:
        return "Invalid selection. Please choose a valid option."

    user_prompt = SYMPTOM_PROMPTS[symptom_key] + " Do not repeat these instructions back. Directly give the advice."
    return generate_response(user_prompt)


def get_response_for_freetext(user_text):
    if check_emergency(user_text):
        return EMERGENCY_RESPONSE
    return generate_response(f"The user says: '{user_text}'. Respond following the rules.")