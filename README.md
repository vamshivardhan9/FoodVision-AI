# Deep-Learning-Food-Classification-using-MultiModels
# 🍱 Food Classification System

A deep learning-based **Food Classification System** that identifies food items from images and provides nutritional information. The project uses multiple CNN-based models for food image classification and Redis for storing and retrieving nutrition data and model metrics.

---

## 📌 Project Overview

The Food Classification System takes a food image as input and predicts the food category using trained deep learning models.

After identifying the food item, the application retrieves its nutritional information from a JSON dataset stored in Redis.

### Main Features

* 📷 Upload a food image
* 🤖 Food classification using deep learning
* 🧠 Multiple trained models
* 📊 Model performance/metrics
* 🥗 Nutrition information
* ⚡ Redis-based data storage
* 🌐 Flask web application
* 💾 Keras model (`.keras`) support
* 🎨 Web-based result page

---

## 🏗️ Project Architecture

```text
                 ┌─────────────────┐
                 │   User Uploads  │
                 │   Food Image    │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │   Flask Web App │
                 └────────┬────────┘
                          │
                          ▼
              ┌───────────────────────┐
              │ Image Preprocessing   │
              │ Resize / Normalize    │
              └───────────┬───────────┘
                          │
                          ▼
        ┌─────────────────────────────────┐
        │       Deep Learning Models      │
        │                                 │
        │  CNN  │  VGG16  │  ResNet50     │
        │                                 │      
        └─────────────────┬───────────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ Predicted Food  │
                 │     Class       │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │      Redis      │
                 │ Nutrition Data  │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ Results Page    │
                 │ Food + Nutrition│
                 └─────────────────┘
```

---

## 🛠️ Technologies Used

| Technology | Purpose                    |
| ---------- | -------------------------- |
| Python     | Main programming language  |
| TensorFlow | Deep learning framework    |
| Keras      | Model building and loading |
| OpenCV     | Image processing           |
| NumPy      | Numerical operations       |
| Flask      | Web application            |
| Redis      | Data storage/cache         |
| JSON       | Nutrition data             |
| HTML/CSS   | Frontend                   |
| Git/GitHub | Version control            |

---

## 🧠 Deep Learning Models

The project can use multiple models for food classification.

### 1. CNN

A custom Convolutional Neural Network is used for image classification.

Typical architecture:

```text
Input Image
     ↓
Convolution
     ↓
ReLU
     ↓
Pooling
     ↓
Convolution
     ↓
ReLU
     ↓
Pooling
     ↓
Flatten
     ↓
Dense
     ↓
Output Classes
```

### 2. VGG16

VGG16 is a pretrained convolutional neural network commonly used for image classification and transfer learning.

### 3. ResNet50

ResNet50 uses residual connections to make training deeper networks easier.



## 📁 Project Structure

Example project structure:

```text
Food_Classification/
│
├── main.py
├── app.py
├── metrics.py
│
├── index.html
├── results.html
│
├── nutrition.json
│
├── models/
│   ├── cnn_model.keras
│   ├── vgg16_model.keras
│   ├── resnet50_model.keras
│
│
├── static/
│   ├── css/
│   ├── js/
│   └── food_images/
│
├── templates/
│   ├── index.html
│   └── results.html
│
├── requirements.txt
└── README.md
```

> Adjust the filenames and folders to match your actual project structure.

---

## ⚙️ Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/Food_Classification.git
```

Move into the project:

```bash
cd Food_Classification
```

---

### Step 2: Create a Virtual Environment

Windows:

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

You should see:

```text
(.venv)
```

in your terminal.

---

### Step 3: Install Dependencies

Install the required packages:

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file, common packages include:

```bash
pip install flask tensorflow opencv-python numpy redis pillow
```

---

## 🔴 Redis Setup

Redis is used to store nutrition information and model metrics.

The application connects to Redis using:

```python
import redis

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    db=0,
    decode_responses=True
)
```

### Check Redis Connection

Run:

```python
redis_client.ping()
```

If Redis is working correctly:

```text
True
```

will be returned.

---

## 🥗 Nutrition Data

Nutrition information is maintained in:

```text
nutrition.json
```

Example:

```json
{
    "pizza": {
        "calories": 266,
        "protein": 11,
        "carbohydrates": 33,
        "fat": 10
    }
}
```

The JSON data can be stored in Redis under a key such as:

```text
nutrition
```

Example:

```python
import json
import redis

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    db=0,
    decode_responses=True
)

with open("nutrition.json", "r", encoding="utf-8") as file:
    food_data = json.load(file)

redis_client.set(
    "nutrition",
    json.dumps(food_data)
)

print("Food data stored successfully")
```

---

## 🖼️ Image Processing

The uploaded image is processed before being passed to the model.

Typical preprocessing includes:

1. Read image
2. Resize image
3. Convert color format
4. Normalize pixel values
5. Add batch dimension

Example:

```python
import cv2
import numpy as np

image = cv2.imread("image.jpg")

image = cv2.resize(image, (224, 224))

image = image.astype("float32") / 255.0

image = np.expand_dims(image, axis=0)
```

The input size should match the model's expected input size.

---

## 🤖 Loading a Keras Model

A `.keras` model can be loaded using:

```python
from tensorflow.keras.models import load_model

model = load_model("models/cnn_model.keras")
```

Prediction:

```python
prediction = model.predict(image)
```

The predicted class can then be obtained using the class mapping used during training.

---

## 🌐 Running the Flask Application

Start the Flask application:

```bash
python app.py
```

or, depending on your project:

```bash
python main.py
```

You should see something similar to:

```text
Running on http://127.0.0.1:5000
```

Open the address in your browser:

```text
http://127.0.0.1:5000
```

---

## 🔄 Application Workflow

```text
1. User opens website
          ↓
2. User uploads food image
          ↓
3. Flask receives image
          ↓
4. Image preprocessing
          ↓
5. Image sent to trained models
          ↓
6. Food class predicted
          ↓
7. Nutrition data retrieved from Redis
          ↓
8. Results displayed
```

---

## 📊 Model Metrics

The project can maintain performance metrics for different models.

Example:

```text
CNN
Accuracy: XX%

VGG16
Accuracy: XX%

ResNet50
Accuracy: XX%

MobileNet
Accuracy: XX%
```

Metrics can be stored in Redis for later retrieval.

Example Redis keys:

```text
cnn_metrics
vgg16_metrics
resnet50_metrics
mobilenet_metrics
```

---

## 🧪 Testing

Test the application with different food images.

Check:

* Image upload
* Image preprocessing
* Model prediction
* Predicted class
* Nutrition lookup
* Redis connection
* Results page
* Multiple model predictions

---

## 🐛 Common Issues

### Redis Connection Error

If you see:

```text
Connection refused
```

make sure the Redis server is running.

Check Redis with:

```bash
redis-cli ping
```

Expected:

```text
PONG
```

---

### Pillow Not Installed

If you see:

```text
WARNING: Package(s) not found: Pillow
```

install it:

```bash
pip install Pillow
```

Then update requirements:

```bash
pip freeze > requirements.txt
```

---

### Model File Not Found

If you see:

```text
FileNotFoundError
```

check that the `.keras` file exists and that the path is correct.

Example:

```python
model = load_model("models/cnn_model.keras")
```

---

### Redis `HELLO` Error

If Redis reports:

```text
unknown command `HELLO`
```

your Redis server may be an older/incompatible Redis implementation.

Check the server version:

```bash
redis-cli INFO server
```

or:

```bash
redis-server --version
```

The Python Redis client and Redis server need to be compatible.

---

## 📦 Requirements

Example `requirements.txt`:

```text
Flask
tensorflow
numpy
opencv-python
Pillow
redis
```

Generate the exact dependency list from your virtual environment with:

```bash
pip freeze > requirements.txt
```

---

## 🚀 Future Improvements

* Improve classification accuracy
* Add more food classes
* Add confidence scores
* Add top-5 predictions
* Compare all models on one results page
* Add user authentication
* Add food history
* Add calorie tracking
* Deploy the application to the cloud
* Add REST API support
* Improve frontend UI
* Add database support for user-specific results

---

## 🔐 Important

Do not upload sensitive information such as:

```text
.env
API keys
passwords
private credentials
large datasets
```

to GitHub.

Use `.gitignore`:

```text
.venv/
__pycache__/
.env
*.pyc
```

---

## 👨‍💻 Author

**Vamshi Vardhan Nagati**

Food Classification System using Deep Learning, Flask, and Redis.

---

## ⭐ Project Summary

This project demonstrates how **Deep Learning + Computer Vision + Flask + Redis** can be combined to build a practical food recognition application.

The system:

```text
Food Image
    ↓
Computer Vision
    ↓
Deep Learning
    ↓
Food Classification
    ↓
Redis
    ↓
Nutrition Information
    ↓
Web Results
```

---


