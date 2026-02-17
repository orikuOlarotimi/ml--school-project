import os
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify
import tensorflow as tf
from werkzeug.utils import secure_filename
import tempfile

# Initialize Flask app
app = Flask(__name__)

# Load model
model_path = os.path.join(os.path.dirname(__file__), "models", "plant_disease_model.h5")
model = tf.keras.models.load_model(model_path)

# Load disease info CSV safely
csv_path = os.path.join(os.path.dirname(__file__), "data", "disease_info.csv")
disease_df = pd.read_csv(csv_path, encoding='ISO-8859-1')
# Convert to dictionary using index
disease_info = disease_df.set_index("index").to_dict(orient="index")

# List of class names (matching your model)
# class_names = list(disease_info.keys())

# Prediction function
def predict_disease(img_path):
    img = tf.keras.utils.load_img(img_path, target_size=(224, 224))
    x = tf.keras.utils.img_to_array(img)
    x = x / 255.0
    x = np.expand_dims(x, axis=0)

    preds = model.predict(x)
    class_index = np.argmax(preds)
    info = disease_info.get(class_index, {
        "disease_name": "Unknown",
        "description": "No info available",
        "Possible Steps": "Consult an expert"
    })
    return info

# REST endpoint


@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    filename = secure_filename(file.filename)
    temp_dir = tempfile.gettempdir()  # Returns /tmp on Linux/Mac or C:\Users\…\AppData\Local\Temp on Windows
    temp_path = os.path.join(temp_dir, filename)
    file.save(temp_path)

    # Predict
    result = predict_disease(temp_path)

    # Remove temp file if desired
    os.remove(temp_path)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
