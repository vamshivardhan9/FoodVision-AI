import os

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

CLASS_NAMES = [
    "Baked Potato",
    "Crispy Chicken",
    "Donut",
    "Fries",
    "Hot Dog",
    "Sandwich",
    "Taco",
    "Taquito",
    "apple_pie",
    "burger",
    "butter_naan",
    "chai",
    "chapati",
    "cheesecake",
    "chicken_curry",
    "chole_bhature",
    "dal_makhani",
    "dhokla",
    "fried_rice",
    "ice_cream",
    "idli",
    "jalebi",
    "kaathi_rolls",
    "kadai_paneer",
    "kulfi",
    "masala_dosa",
    "momos",
    "omelette",
    "paani_puri",
    "pakode",
    "pav_bhaji",
    "pizza",
    "samosa",
    "sushi"
]
FOOD_IMAGE_MAP = {

    "Baked Potato": "baked_potato",
    "Crispy Chicken": "crispy_chicken",
    "Donut": "donuts",
    "Fries": "fries",
    "Hot Dog": "hot_dog",
    "Sandwich": "sandwich",
    "Taco": "taco",
    "Taquito": "taquitos",

    "apple_pie": "apple_pie",
    "burger": "burger",
    "butter_naan": "butter_naan",
    "chai": "chai",
    "chapati": "chapati",
    "cheesecake": "cheese_cake",
    "chicken_curry": "chicken_curry",
    "chole_bhature": "chole_bature",
    "dal_makhani": "dal_makhani",
    "dhokla": "dhokla",
    "fried_rice": "fried_rice",
    "ice_cream": "ice_cream",
    "idli": "idly",
    "jalebi": "jalebi",
    "kaathi_rolls": "kaathi_rolls",
    "kadai_paneer": "kadai_paneer",
    "kulfi": "kulfi",
    "masala_dosa": "masala_dosa",
    "momos": "momos",
    "omelette": "omlette",
    "paani_puri": "paani_puri",
    "pakode": "pakode",
    "pav_bhaji": "pav_bhaaji",
    "pizza": "pizza",
    "samosa": "samosa",
    "sushi": "sushi"
}
NUTRITION_KEY_MAP = {
    "Baked Potato": "baked_potato",
    "Crispy Chicken": "crispy_chicken",
    "Donut": "donuts",
    "Fries": "fries",
    "Hot Dog": "hot_dog",
    "Sandwich": "sandwich",
    "Taco": "taco",
    "Taquito": "taquitos",
    "apple_pie": "apple_pie",
    "burger": "burger",
    "butter_naan": "butter_naan",
    "chai": "chai",
    "chapati": "chapati",
    "cheesecake": "cheese_cake",
    "chicken_curry": "chicken_curry",
    "chole_bhature": "chole_bature",
    "dal_makhani": "dal_makhani",
    "dhokla": "dhokla",
    "fried_rice": "fried_rice",
    "ice_cream": "ice_cream",
    "idli": "idly",
    "jalebi": "jalebi",
    "kaathi_rolls": "kaathi_rolls",
    "kadai_paneer": "kadai_paneer",
    "kulfi": "kulfi",
    "masala_dosa": "masala_dosa",
    "momos": "momos",
    "omelette": "omlette",
    "paani_puri": "paani_puri",
    "pakode": "pakode",
    "pav_bhaji": "pav_bhaaji",
    "pizza": "pizza",
    "samosa": "samosa",
    "sushi": "sushi"
}
MODEL_METRIC_KEYS = {
    "cnn": "cnn_metrics",
    "vgg16": "vgg16_metrics",
    "resnet50": "resnet50_metrics"
}

def normalize_class_name(class_name):
    if not class_name:
        return None
    class_name = class_name.strip()
    for project_name in CLASS_NAMES:
        if project_name.lower() == class_name.lower():
            return project_name
    return class_name

def get_food_image_url(class_name):

    image_name = FOOD_IMAGE_MAP.get(class_name)

    if not image_name:
        print(f"[WARNING] No image mapping for: {class_name}")
        return None

    food_image_folder = os.path.join(
        BASE_DIR,
        "static",
        "food_images"
    )

    # Check actual files in the folder
    for filename in os.listdir(food_image_folder):

        name, extension = os.path.splitext(filename)

        if (
            name.lower() == image_name.lower()
            and extension.lower() in [".jpg", ".jpeg"]
        ):

            print(
                f"[IMAGE FOUND] {class_name} -> {filename}"
            )

            return f"/static/food_images/{filename}"

    print(
        f"[WARNING] Image not found for "
        f"{class_name} -> {image_name}"
    )

    return None
# ============================================================
# 6. HELPER FUNCTION - REDIS NUTRITION KEY
# ============================================================

def get_nutrition_key(class_name):

    return NUTRITION_KEY_MAP.get(class_name)


# ============================================================
# 7. HELPER FUNCTION - REDIS METRIC KEY
# ============================================================

def get_metric_redis_key(model_name):

    return MODEL_METRIC_KEYS.get(
        model_name.lower()
    )