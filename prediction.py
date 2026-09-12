import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

from tensorflow.keras.applications.vgg16 import preprocess_input as vgg_preprocess
from tensorflow.keras.applications.resnet50 import preprocess_input as resnet_preprocess

def predict_vgg(path):
    model=load_model('./models/vgg16.keras',compile=False)
    img = image.load_img(path, target_size=(256, 256),color_mode='rgb')
    # 3. Convert image pixels into a numpy array
    img_array = image.img_to_array(img)
    # 4. Add a fourth dimension (batch size) since models expect batches: (1, 224, 224, 3)
    img_array = np.expand_dims(img_array, axis=0)
    # 5. Apply VGG16 specific preprocessing (zero-centering, channel scaling)
    img_array = vgg_preprocess(img_array)
    # 6. Run inference
    predictions = model.predict(img_array,verbose=0)
    # 7. Extract the predicted class index
    predicted_index = np.argmax(predictions[0])
    confidence=float(predictions[0][predicted_index])
    return predicted_index,confidence

def predict_custom(path):
    model = load_model('./models/cnn.keras')
    img = image.load_img(path, target_size=(256, 256),color_mode='rgb')
    # 3. Convert image pixels into a numpy array
    img_array = image.img_to_array(img)
    # 4. Add a fourth dimension (batch size) since models expect batches: (1, 224, 224, 3)
    img_array = np.expand_dims(img_array, axis=0)
    # 5. Apply Custom specific preprocessing (zero-centering, channel scaling)
    img_array = img_array / 255.0
    # 6. Run inference
    predictions = model.predict(img_array,verbose=0)
    # 7. Extract the predicted class index
    predicted_index = np.argmax(predictions[0])
    confidence = float(predictions[0][predicted_index])
    return predicted_index, confidence

def predict_resnet(path):
    model=load_model('./models/resnet.keras')
    img = image.load_img(path, target_size=(256, 256),color_mode='rgb')
    # 3. Convert image pixels into a numpy array
    img_array = image.img_to_array(img)
    # 4. Add a fourth dimension (batch size) since models expect batches: (1, 224, 224, 3)
    img_array = np.expand_dims(img_array, axis=0)
    # 5. Apply VGG16 specific preprocessing (zero-centering, channel scaling)
    img_array = resnet_preprocess(img_array)
    # 6. Run inference
    predictions = model.predict(img_array,verbose=0)
    # 7. Extract the predicted class index
    predicted_index = np.argmax(predictions[0])
    confidence = float(predictions[0][predicted_index])
    return predicted_index, confidence