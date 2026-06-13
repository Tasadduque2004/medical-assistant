import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from prompts import SYMPTOM_RESPONSES, EMERGENCY_KEYWORDS, EMERGENCY_RESPONSE

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


def get_response_for_symptom(symptom_key):
    if symptom_key not in SYMPTOM_RESPONSES:
        return "Invalid selection. Please choose a valid option."

    response = SYMPTOM_RESPONSES[symptom_key]
    return response + "\n\n*This is general advice only. Please consult a doctor or health worker for proper care.*"


def get_response_for_freetext(user_text):
    if check_emergency(user_text):
        return EMERGENCY_RESPONSE

    prompt = f"Answer this health question in simple words: {user_text}"
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)
    outputs = model.generate(
        **inputs,
        max_new_tokens=150,
        min_length=20,
        repetition_penalty=2.5,
        no_repeat_ngram_size=3,
        num_beams=4
    )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
    return response + "\n\n*This is general advice only. Please consult a doctor or health worker for proper care.*"