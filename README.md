# Deep-Learning-Food-Classification-using-MultiModels
# 🍽️ FoodVision AI — Food Classification System

**FoodVision AI** is a Deep Learning and Computer Vision web application that identifies food items from uploaded images.

The application supports **three classification models — CNN, VGG16, and ResNet50** — and returns the predicted food class, confidence, model-specific metrics, food image, and nutritional information.

The backend is built with **Python and Flask**, while **Redis** is used to provide food-class and nutrition data.

---

## 🚀 Features

* Upload a food image through a web interface
* Select a classification model
* Food classification using:

  * CNN
  * VGG16
  * ResNet50
* Supports **34 food classes**
* Displays prediction confidence
* Displays predicted food class
* Allows selection of the actual food class
* Displays model metrics for the predicted class
* Retrieves nutrition information
* Displays an image of the predicted food
* Redis connectivity/health checking
* REST API endpoints for prediction, nutrition, and food classes
* Maximum upload size of 10 MB
* Supports JPG, JPEG, PNG, and WebP images

The Flask application exposes `/predict`, `/health`, `/food-classes`, and nutrition-related endpoints.

---

# 🧠 Models

FoodVision AI currently supports three models:

| Model    | Input Size | Output Classes |
| -------- | ---------: | -------------: |
| CNN      |  240 × 240 |             34 |
| VGG16    |  256 × 256 |             34 |
| ResNet50 |  256 × 256 |             34 |

The input dimensions and model names are defined directly in the application.

---

## 🔹 CNN Architecture

The custom CNN contains convolution, max-pooling, flattening, and dense layers.

```text
Input
240 × 240 × 3
      ↓
Conv2D – 12 filters
      ↓
MaxPooling
      ↓
Conv2D – 6 filters
      ↓
MaxPooling
      ↓
Conv2D – 3 filters
      ↓
MaxPooling
      ↓
Flatten
      ↓
Dense – 8
      ↓
Dense – 4
      ↓
Dense – 3
      ↓
Dense – 34
      ↓
Softmax
```

The CNN is reconstructed from the supplied `cnn.weights.h5` weights and has a 34-neuron softmax output layer.

---

## 🔹 VGG16

The VGG16 model uses a VGG-style convolutional architecture with five convolution blocks.

```text
Input
256 × 256 × 3
      ↓
Convolution Blocks
      ↓
Max Pooling
      ↓
Feature Extraction
      ↓
Classification Layers
      ↓
34 Food Classes
```

The application reconstructs the VGG-style network from the supplied weights.

---

## 🔹 ResNet50

ResNet50 is the third classification model supported by the application.

```text
Input Image
    ↓
ResNet50
    ↓
Feature Extraction
    ↓
Classification
    ↓
34 Food Classes
```

The model can be selected directly from the web interface along with CNN and VGG16.

---

# 🍔 Supported Food Classes

The current model contains **34 output classes**:

```text
1.  Baked Potato
2.  Pakode
3.  chapati
4.  chicken_curry
5.  Kulfi
6.  Taco
7.  burger
8.  momos
9.  Donut
10. butter_naan
11. Masala dosa
12. Fries
13. dal_makhani
14. jalebi
15. chole_bhature
16. pav_bhaji
17. pizza
18. samosa
19. kaathi_rolls
20. fried_rice
21. ice_cream
22. dhokla
23. Crispy Chicken
24. Sandwich
25. chai
26. sushi
27. idli
28. apple_pie
29. kadai_paneer
30. Hot Dog
31. cheesecake
32. Taquito
33. omelette
34. paani_puri
```

These classes are defined in the Flask backend and correspond to the 34 output neurons in the supplied model weights.

---

# 🏗️ System Architecture

```text
                 ┌────────────────────┐
                 │      User          │
                 └─────────┬──────────┘
                           │
                           ▼
                 ┌────────────────────┐
                 │   Web Interface    │
                 │     index.html     │
                 └─────────┬──────────┘
                           │
                     Upload Image
                           │
                           ▼
                 ┌────────────────────┐
                 │    Flask API       │
                 │      app.py        │
                 └─────────┬──────────┘
                           │
                           ▼
                 ┌────────────────────┐
                 │ Image Preprocessing│
                 └─────────┬──────────┘
                           │
                           ▼
        ┌────────────────────────────────────┐
        │          Classification            │
        │                                    │
        │   CNN     VGG16      ResNet50     │
        └────────────────┬───────────────────┘
                         │
                         ▼
                 ┌────────────────────┐
                 │ Predicted Food     │
                 │ + Confidence       │
                 └─────────┬──────────┘
                           │
             ┌─────────────┴─────────────┐
             ▼                           ▼
     ┌───────────────┐           ┌───────────────┐
     │ Redis / JSON  │           │ Model Metrics │
     │ Nutrition     │           │ JSON Files    │
     └───────┬───────┘           └───────┬───────┘
             │                           │
             └─────────────┬─────────────┘
                           ▼
                 ┌────────────────────┐
                 │   results.html     │
                 │                    │
                 │ Food               │
                 │ Confidence         │
                 │ Nutrition          │
                 │ Metrics            │
                 └────────────────────┘
```

---

# 📁 Project Files

The main backend configuration uses the following files:

```text
Food_Classification/
│
├── app.py
│
├── cnn.weights.h5
├── vgg16.weights.h5
├── resnet.weights.h5
│
├── CNN_metrics.json
├── VGG16_metrics.json
├── ResNet_metrics.json
│
├── nutrition.json
│
├── index.html
├── results.html
│
├── uploads/
│
└── static/
    └── food_images/
```

The backend maps the three weight files and three corresponding metric files as follows.

---

# 🛠️ Technologies Used

| Technology | Purpose                     |
| ---------- | --------------------------- |
| Python     | Application development     |
| TensorFlow | Deep Learning               |
| Keras      | Neural network models       |
| Flask      | Web backend/API             |
| Redis      | Nutrition and food data     |
| NumPy      | Numerical processing        |
| OpenCV     | Image processing            |
| HTML       | Frontend                    |
| CSS        | UI styling                  |
| JavaScript | Frontend interaction        |
| JSON       | Nutrition and model metrics |

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone <your-repository-url>
```

Then:

```bash
cd Food_Classification
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

---

## 3. Install Dependencies

If `requirements.txt` is available:

```bash
pip install -r requirements.txt
```

Otherwise, install the main packages:

```bash
pip install flask tensorflow numpy opencv-python pillow redis
```

---

# 🔴 Redis Configuration

The application connects to Redis on:

```text
Host: localhost
Port: 6379
Database: 0
```

The connection configuration in the project is:

```python
redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True,
    db=0
)
```

The application calls `ping()` to check whether Redis is available.

---

# 🥗 Nutrition Data

Nutrition information is loaded from Redis using the key:

```text
nutrition
```

If Redis is unavailable, the application can fall back to the local nutrition JSON file.

Food names are normalized before performing the nutrition lookup. For example:

```text
Baked Potato → Baked_Potato
Crispy Chicken → Crispy_Chicken
Hot Dog → Hot_Dog
Masala Dosa → masala_dosa
```

This prevents differences in food-name formatting from breaking the nutrition lookup.

---

# 📊 Model Metrics

The application loads model metrics from:

```text
CNN_metrics.json
VGG16_metrics.json
ResNet_metrics.json
```

Metrics can be retrieved for a particular predicted food class.

For example:

```text
Model: CNN
Food Class: pizza
        ↓
CNN_metrics.json
        ↓
Pizza metrics
```

The backend also supports alternative class naming such as spaces and underscores.

---

# 🌐 Web Application

Start the application with:

```bash
python app.py
```

The Flask server runs on:

```text
http://127.0.0.1:5000
```

The application is configured to listen on all interfaces at port `5000` while running in debug mode.

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

# 🖼️ Using the Application

## Step 1 — Upload Image

Select a food image from your computer.

Supported formats:

```text
JPG
JPEG
PNG
WebP
```

The backend allows a maximum request size of **10 MB**.

---

## Step 2 — Select Actual Food Class

The UI provides an option to select the actual food class.

This can be used to compare the actual class against the predicted class and retrieve corresponding metrics.

---

## Step 3 — Select Model

Choose one:

```text
CNN
VGG16
ResNet50
```

The frontend provides buttons for all three models.

---

## Step 4 — Predict

Click:

```text
Predict Food
```

The image is sent to the Flask `/predict` endpoint.

The backend:

```text
Upload Image
     ↓
Validate Image
     ↓
Select Model
     ↓
Load Model
     ↓
Preprocess Image
     ↓
Run Prediction
     ↓
Find Predicted Class
     ↓
Calculate Confidence
     ↓
Get Nutrition
     ↓
Get Metrics
     ↓
Return Result
```

The prediction endpoint returns the predicted class, confidence, model, nutrition, metrics, food image, and uploaded image information.

---

# 🔌 API Endpoints

## `GET /`

Displays the main prediction page.

```text
GET /
```

---

## `GET /results`

Displays the results page.

```text
GET /results
```

---

## `GET /health`

Checks the application and Redis status.

Example response:

```json
{
    "status": "running",
    "redis": true,
    "number_of_classes": 34,
    "models": [
        "cnn",
        "vgg16",
        "resnet50"
    ]
}
```

The health endpoint reports Redis status, the number of classes, available food data, and supported models.

---

## `GET /food-classes`

Returns the available food classes.

Example:

```json
{
    "success": true,
    "count": 34,
    "classes": []
}
```

---

## `GET /nutrition/<food_class>`

Returns nutrition information for a food class.

Example:

```text
GET /nutrition/pizza
```

Possible response:

```json
{
    "success": true,
    "food": "pizza",
    "nutrition": {}
}
```

---

## `POST /predict`

Performs food classification.

Required:

```text
image
```

Optional:

```text
model
actual_class
```

Supported model values:

```text
cnn
vgg16
resnet50
```

---

# 📤 Prediction Response

A successful prediction contains information such as:

```json
{
    "success": true,
    "model": "cnn",
    "predicted_class": "pizza",
    "predicted_index": 16,
    "confidence": 0.95,
    "actual_class": "pizza",
    "actual_metrics": {},
    "predicted_metrics": {},
    "nutrition": {},
    "nutrition_redis_key": "pizza",
    "food_image": "",
    "uploaded_image": ""
}
```

The exact nutrition and metrics values depend on the corresponding project data files and Redis contents.

---

# 🔄 Complete Workflow

```text
User
 │
 ▼
Open FoodVision AI
 │
 ▼
Upload Food Image
 │
 ▼
Select Actual Food Class
 │
 ▼
Select CNN / VGG16 / ResNet50
 │
 ▼
Click "Predict Food"
 │
 ▼
Flask /predict
 │
 ▼
Image Preprocessing
 │
 ▼
Selected Deep Learning Model
 │
 ▼
Prediction
 │
 ▼
Predicted Food Class
 │
 ├──────────────► Confidence
 │
 ├──────────────► Model Metrics
 │
 ├──────────────► Nutrition Data
 │
 └──────────────► Food Image
 │
 ▼
Results Page
```

---

# 🧪 Testing

Before testing predictions, verify Redis:

```bash
redis-cli ping
```

Expected:

```text
PONG
```

Then start Flask:

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

Test with different food images and compare the predictions from:

```text
CNN
VGG16
ResNet50
```

---

# ⚠️ Common Problems

## Redis Not Connected

Check whether Redis is running:

```bash
redis-cli ping
```

Expected:

```text
PONG
```

If Redis is not running, nutrition and class-related functionality may not work as intended.

---

## Model Weights Not Found

Make sure these files exist in the project directory:

```text
cnn.weights.h5
vgg16.weights.h5
resnet.weights.h5
```

The application explicitly maps these filenames to the corresponding models.

---

## Incorrect Food Class

The model can only predict the 34 classes defined by the application.

An image outside these categories may still be forced into one of the available classes. **The prediction should therefore not be treated as proof that the image actually belongs to the predicted food category.**

---

# 🔐 Security Notes

For production deployment:

* Disable Flask debug mode
* Validate uploaded file contents, not only extensions
* Use unique filenames for uploads
* Restrict Redis access
* Do not expose Redis directly to the public internet
* Store secrets in environment variables
* Configure production logging
* Use a production WSGI server

---

# 🚀 Future Improvements

1. Add more food classes.
2. Improve model accuracy.
3. Add top-5 predictions.
4. Add model comparison on the same image.
5. Add prediction history.
6. Add user authentication.
7. Add calorie tracking.
8. Add charts for nutrition information.
9. Deploy the application to a cloud server.
10. Add automated model evaluation.
11. Add confidence thresholding so uncertain predictions can be rejected instead of blindly assigning a class.
12. Add a proper database for users and prediction history.

---

# 📌 Project Summary

**FoodVision AI** combines:

```text
Computer Vision
       +
Deep Learning
       +
Flask
       +
Redis
       +
Nutrition Data
       =
Food Classification Web Application
```

The system accepts a food image, uses one of three deep-learning models to classify it into one of 34 food categories, and then combines the prediction with nutrition and model-metric information before presenting the result through the web interface.

---

## 👨‍💻 Author

**Vamshi Vardhan Nagati**

### FoodVision AI

> Deep Learning Food Classification System
