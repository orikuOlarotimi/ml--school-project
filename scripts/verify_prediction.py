import numpy as np
import pandas as pd
import tensorflow as tf

import os

# Define Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "plant_disease_model.h5")
CSV_PATH = os.path.join(BASE_DIR, "data", "disease_info.csv")
TEST_IMG_PATH = os.path.join(BASE_DIR, "tests", "testimage.jpg")

# Load trained model
print(f"Loading model from: {MODEL_PATH}")
model = tf.keras.models.load_model(MODEL_PATH)

# Load disease CSV
print(f"Loading CSV from: {CSV_PATH}")
disease_df = pd.read_csv(CSV_PATH, encoding="latin1")
disease_info = disease_df.set_index("index").to_dict(orient="index")

def predict_disease(img_path):
    if not os.path.exists(img_path):
        return {"error": f"Image not found at {img_path}"}
        
    img = tf.keras.utils.load_img(img_path, target_size=(224, 224))
    x = tf.keras.utils.img_to_array(img)
    x = x / 255.0
    x = np.expand_dims(x, axis=0)

    preds = model.predict(x)
    class_index = int(np.argmax(preds))

    info = disease_info.get(class_index, {
        "disease_name": "Unknown",
        "description": "No info available",
        "Possible Steps": "Consult an expert"
    })

    return info


# Test
if __name__ == "__main__":
    result = predict_disease(TEST_IMG_PATH)
    print(result)
