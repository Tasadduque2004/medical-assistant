SYMPTOM_RESPONSES = {
    "1": """**Managing Mild Fever**
1. Rest: Lie down and avoid physical activity until fever reduces.
2. Fluids: Drink plenty of water, ORS, or coconut water to stay hydrated.
3. Food: Eat light, easy-to-digest food like khichdi or soup.
4. Wet Cloth: Place a damp cloth on the forehead to help cool the body.
5. Warning Signs: See a doctor if fever stays above 102°F for more than 2 days, or if there is difficulty breathing, rashes, or confusion.""",

    "2": """**Managing Cough and Cold**
1. Warm Fluids: Drink warm water, tea, or soup to soothe the throat.
2. Steam: Inhale steam from hot water to ease congestion.
3. Salt Water Gargle: Gargle with warm salt water for sore throat.
4. Rest: Get plenty of sleep to help the body recover.
5. Warning Signs: See a doctor if cough lasts more than 2 weeks, or if there is chest pain, high fever, or difficulty breathing.""",

    "3": """**Managing Stomach Pain / Upset Stomach**
1. Hydration: Drink ORS or boiled water to prevent dehydration.
2. Diet: Eat bland food like rice, banana, and toast; avoid spicy/oily food.
3. Rest: Avoid physical strain and rest in a comfortable position.
4. Avoid: Skip dairy, caffeine, and alcohol until recovered.
5. Warning Signs: See a doctor if there is severe pain, blood in stool, continuous vomiting, or fever.""",

    "4": """**First Aid for Minor Cuts, Wounds, or Burns**
1. Clean: Wash the wound gently with clean water and mild soap.
2. Disinfect: Apply an antiseptic if available.
3. Cover: Use a clean cloth or bandage to cover the wound.
4. For Burns: Run cool (not ice) water over the burn for several minutes.
5. Warning Signs: See a doctor if the wound is deep, won't stop bleeding, or shows signs of infection (redness, swelling, pus).""",

    "5": """**Managing Headache or Body Pain**
1. Rest: Sit or lie down in a quiet, dark room.
2. Hydration: Drink enough water, as dehydration can cause headaches.
3. Cold Compress: Apply a cold cloth to the forehead for headaches.
4. Gentle Stretching: For body pain, gentle stretching can help.
5. Warning Signs: See a doctor if pain is severe, sudden, or comes with vision changes, vomiting, or confusion.""",

    "6": """**General Hygiene and Nutrition Tips**
1. Hand Washing: Wash hands with soap before eating and after using the toilet.
2. Clean Water: Drink boiled or filtered water.
3. Balanced Diet: Include vegetables, fruits, grains, and protein in meals.
4. Food Storage: Keep food covered and stored properly to avoid contamination.
5. Regular Checkups: Visit a health worker periodically, even when feeling well."""
}

EMERGENCY_KEYWORDS = [
    "chest pain", "difficulty breathing", "unconscious", "severe bleeding",
    "not breathing", "seizure", "fainted", "snake bite", "poisoning",
    "heart attack", "stroke", "accident"
]

EMERGENCY_RESPONSE = (
    "**This sounds like a medical EMERGENCY.**\n"
    "Please go to the nearest hospital IMMEDIATELY or call emergency services / ASHA worker.\n"
    "Do not wait. Get help now."
)