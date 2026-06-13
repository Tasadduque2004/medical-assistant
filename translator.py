from deep_translator import GoogleTranslator

LANGUAGES = {
    "1": ("English", "en"),
    "2": ("Hindi", "hi"),
    "3": ("Kannada", "kn"),
    "4": ("Tamil", "ta"),
    "5": ("Telugu", "te")
}

def translate_text(text, target_lang_code):
    if target_lang_code == "en":
        return text
    try:
        translated = GoogleTranslator(source="en", target=target_lang_code).translate(text)
        return translated
    except Exception:
        return f"[Translation failed, showing English]\n{text}"