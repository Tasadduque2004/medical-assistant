import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from prompts import SYMPTOM_PROMPTS, EMERGENCY_KEYWORDS, EMERGENCY_RESPONSE

MODEL_NAME = "google/flan-t5-base"


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
    inputs = tokenizer(user_prompt, return_tensors="pt", truncation=True, max_length=512)
    outputs = model.generate(
        **inputs,
        max_new_tokens=250,
        min_length=80,
        repetition_penalty=2.5,
        no_repeat_ngram_size=3,
        num_beams=4
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True).strip()


def get_response_for_symptom(symptom_key):
    if symptom_key not in SYMPTOM_PROMPTS:
        return "Invalid selection. Please choose a valid option."

    user_prompt = SYMPTOM_PROMPTS[symptom_key]
    response = generate_response(user_prompt)
    return response + "\n\nThis is general advice only. Please consult a doctor or health worker for proper care."


def get_response_for_freetext(user_text):
    if check_emergency(user_text):
        return EMERGENCY_RESPONSE
    return generate_response(f"The user says: '{user_text}'. Respond following the rules.")