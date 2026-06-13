from transformers import pipeline
from prompts import SYSTEM_PROMPT, SYMPTOM_PROMPTS, EMERGENCY_KEYWORDS, EMERGENCY_RESPONSE

MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

print("Loading model... this happens once and may take a few minutes the first time.")
pipe = pipeline(
    "text-generation",
    model=MODEL_NAME,
    torch_dtype="auto",
    device_map="cpu"
)
print("Model loaded successfully.\n")


def check_emergency(user_text):
    text_lower = user_text.lower()
    for keyword in EMERGENCY_KEYWORDS:
        if keyword in text_lower:
            return True
    return False


def generate_response(user_prompt):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_prompt}
    ]

    prompt_text = pipe.tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )

    outputs = pipe(
        prompt_text,
        max_new_tokens=300,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
        eos_token_id=pipe.tokenizer.eos_token_id
    )

    full_text = outputs[0]["generated_text"]
    response = full_text[len(prompt_text):].strip()
    return response


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