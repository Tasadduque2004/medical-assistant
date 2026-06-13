import streamlit as st
from chatbot import get_response_for_symptom
from translator import translate_text, LANGUAGES

st.set_page_config(page_title="AI Medical Assistant", page_icon="🏥")

st.title("🏥 AI Medical Assistant for Rural Health")
st.write("Select your language and symptom to get general health advice.")

# Language selection
lang_options = {name: code for key, (name, code) in LANGUAGES.items()}
lang_name = st.selectbox("Select Language", list(lang_options.keys()))
lang_code = lang_options[lang_name]

# Symptom selection
symptom_options = {
    "Fever": "1",
    "Cough / Cold": "2",
    "Stomach Pain": "3",
    "Minor Cut / Wound / Burn": "4",
    "Headache / Body Pain": "5",
    "General Hygiene / Nutrition Tip": "6"
}

symptom_name = st.selectbox("Select Symptom", list(symptom_options.keys()))
symptom_key = symptom_options[symptom_name]

if st.button("Get Advice"):
    with st.spinner("Generating advice, please wait..."):
        response_text = get_response_for_symptom(symptom_key)
        translated = translate_text(response_text, lang_code)

    st.success("Here's the advice:")
    st.markdown(translated)
    st.warning("This is general advice only. Please consult a doctor or health worker for proper care.")