from chatbot import get_response_for_symptom
from translator import translate_text, LANGUAGES


def show_menu():
    print("\n========================================")
    print("   AI MEDICAL ASSISTANT - RURAL HEALTH")
    print("========================================")
    print("Select your symptom (press button number):")
    print("1. Fever")
    print("2. Cough / Cold")
    print("3. Stomach Pain")
    print("4. Minor Cut / Wound / Burn")
    print("5. Headache / Body Pain")
    print("6. General Hygiene / Nutrition Tip")
    print("0. Exit")
    print("========================================")


def show_language_menu():
    print("\nSelect Language:")
    for key, (name, code) in LANGUAGES.items():
        print(f"{key}. {name}")


def main():
    show_language_menu()
    lang_choice = input("Enter choice: ").strip()
    lang_name, lang_code = LANGUAGES.get(lang_choice, ("English", "en"))
    print(f"Language set to: {lang_name}")

    while True:
        show_menu()
        choice = input("Your selection: ").strip()

        if choice == "0":
            print("Exiting. Stay healthy!")
            break

        print("\nProcessing your request, please wait...\n")

        response_text = get_response_for_symptom(choice)
        translated = translate_text(response_text, lang_code)

        print("------ ASSISTANT RESPONSE ------")
        print(translated)
        print("--------------------------------")


if __name__ == "__main__":
    main()