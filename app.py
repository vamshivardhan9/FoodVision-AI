import os
import json
import uuid
import redis
from flask import Flask,render_template,request,jsonify,send_from_directory
from prediction import predict_custom,predict_vgg,predict_resnet
from mapping import (
    CLASS_NAMES,
    FOOD_IMAGE_MAP,
    NUTRITION_KEY_MAP,
    MODEL_METRIC_KEYS,
    get_food_image_url,
    get_nutrition_key,
    get_metric_redis_key,
    normalize_class_name)

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR,"uploads")

os.makedirs(UPLOAD_FOLDER,exist_ok=True)

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    db=0,
    decode_responses=True
)



food_data = {}
def load_food_data():
    global food_data
    try:
        raw_data = redis_client.get(
            "nutrition"
        )
        if raw_data is None:
            print("[WARNING] nutrition not found in Redis.")
            food_data = {}
            return
        food_data = json.loads(raw_data)
        if not isinstance(food_data,dict):
            raise ValueError("nutrition is not a JSON object")
        print("nutritionloaded from Redis.")
        print("Food classes:",len(food_data))
    except Exception as e:
        print("[ERROR] Redis nutrition:",e)
        food_data = {}
try:
    print("Redis connection:",redis_client.ping())
    load_food_data()
except Exception as e:
    print("[ERROR] Redis connection failed:",e)

performance_data = {}

def get_class_metrics(model_name, class_name):
    if not model_name or not class_name:
        return {}
    try:
        # Normalize class name
        class_name = normalize_class_name(class_name)
        # Get Redis key for model
        redis_key = get_metric_redis_key(model_name)
        if not redis_key:
            print(
                f"[WARNING] No Redis metric key "
                f"for model: {model_name}"
            )
            return {}
        # Get metrics JSON from Redis
        raw_metrics = redis_client.get(redis_key)
        if raw_metrics is None:
            print(
                f"[WARNING] Redis metric key not found: "
                f"{redis_key}"
            )
            return {}
        # Convert JSON string to Python dictionary
        model_metrics = json.loads(raw_metrics)
        if not isinstance(model_metrics, dict):
            print(
                f"[WARNING] Invalid metric format "
                f"in Redis: {redis_key}"
            )
            return {}
        # Get metrics for class
        metrics = model_metrics.get(class_name, {})
        if not metrics:
            print(
                f"[WARNING] Metrics not found: "
                f"{model_name} -> {class_name}"
            )
        return metrics
    except Exception as e:
        print(
            f"[ERROR] get_class_metrics(): {e}"
        )
        return {}

def get_nutrition(class_name):
    if not class_name:
        return {}
    redis_key = get_nutrition_key(class_name)
    if not redis_key:
        print(
            f"[WARNING] Nutrition mapping "
            f"not found: {class_name}"
        )
        return {}
    nutrition = food_data.get(redis_key,{})
    if not nutrition:
        print(
            f"[WARNING] Nutrition data "
            f"not found in Redis: {redis_key}"
        )
    return nutrition

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/results")
def results():
    return render_template("results.html")

@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER,filename)

@app.route("/food-classes",methods=["GET"])
def food_classes():
    try:
        classes = CLASS_NAMES
        return jsonify({
            "success": True,
            "classes": classes,
            "count": len(classes)
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "classes": [],
            "error": str(e)
        }), 500

@app.route("/nutrition/<path:food_class>",methods=["GET"])
def nutrition(food_class):
    food_class = normalize_class_name(food_class)
    nutrition_data = get_nutrition(food_class)
    if not nutrition_data:
        return jsonify({
            "success": False,
            "error": "Food not found"
        }), 404
    return jsonify({
        "success": True,
        "food": food_class,
        "nutrition": nutrition_data
    })

@app.route("/predict", methods=["POST"])
def predict():
    try:
        if "image" not in request.files:
            return jsonify({
                "success": False,
                "error": "No image uploaded."
            }), 400
        uploaded_file = request.files["image"]
        if uploaded_file.filename == "":
            return jsonify({
                "success": False,
                "error": "No image selected."
            }), 400
        model_name = request.form.get(
            "model",
            "cnn"
        ).lower().strip()
        if model_name not in ["cnn","vgg16","resnet50"]:
            return jsonify({
                "success": False,
                "error": "Invalid model selected."
            }), 400
        actual_class = request.form.get(
            "actual_class",
            ""
        ).strip()
        if actual_class:
            actual_class = normalize_class_name(actual_class)
        extension = os.path.splitext(uploaded_file.filename)[1]
        if not extension:
            extension = ".jpg"
        image_filename = (
            str(uuid.uuid4())
            + extension
        )
        image_path = os.path.join(UPLOAD_FOLDER,image_filename)
        uploaded_file.save(image_path)
        if model_name == "cnn":
            prediction_result = predict_custom(image_path)
        elif model_name == "vgg16":
            prediction_result = predict_vgg(image_path)
        elif model_name == "resnet50":
            prediction_result = predict_resnet(image_path)
        else:
            raise ValueError(
                f"Unsupported model: {model_name}"
            )
        if isinstance(prediction_result,tuple):
            predicted_index = int(prediction_result[0])
            if len(prediction_result) > 1:
                confidence = float(prediction_result[1])
            else:
                confidence = 0.0
        else:
            predicted_index = int(prediction_result)
            confidence = 0.0
        if (predicted_index < 0 or predicted_index >= len(CLASS_NAMES)):
            raise ValueError(
                "Invalid predicted class index: "
                f"{predicted_index}"
            )
        predicted_class = CLASS_NAMES[
            predicted_index
        ]
        predicted_class = normalize_class_name(
            predicted_class
        )
        nutrition_redis_key = get_nutrition_key(
            predicted_class
        )
        nutrition_data = {}
        if nutrition_redis_key:
            nutrition_data = food_data.get(
                nutrition_redis_key,
                {}
            )
        food_image_url = get_food_image_url(
            predicted_class
        )
        image_name = FOOD_IMAGE_MAP.get(
            predicted_class,
            ""
        )
        dataset_folder = predicted_class
        predicted_metrics = get_class_metrics(
            model_name,
            predicted_class
        )
        actual_metrics = {}
        if actual_class:
            actual_metrics = get_class_metrics(
                model_name,
                actual_class
            )
        uploaded_image_url = (
            f"/uploads/{image_filename}"
        )
        return jsonify({
            "success": True,
            "model": model_name,
            "predicted_class":
                predicted_class,
            "predicted_index":
                predicted_index,
            "confidence":
                confidence,
            "actual_class":
                actual_class,
            "actual_metrics":
                actual_metrics,
            "predicted_metrics":
                predicted_metrics,
            "nutrition":
                nutrition_data,
            "nutrition_redis_key":
                nutrition_redis_key,
            "food_image":
                food_image_url,
            "image_name":
                image_name,
            "uploaded_image":
                uploaded_image_url,
            "dataset_folder":
                dataset_folder
        })
    except Exception as e:
        print(
            "PREDICTION ERROR:",
            e
        )
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500
@app.route("/health")
def health():
    try:
        redis_status = redis_client.ping()
    except Exception:
        redis_status = False
    return jsonify({
        "status": "running",
        "redis": redis_status,
        "number_of_classes":
            len(CLASS_NAMES),
        "redis_food_classes":
            len(food_data),
        "models": [
            "cnn",
            "vgg16",
            "resnet50"
        ]
    })
if __name__ == "__main__":
    print("http://127.0.0.1:5000")
    app.run(host="0.0.0.0",
        port=5000,
        debug=True )