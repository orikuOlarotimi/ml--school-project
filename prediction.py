import numpy as np
import pandas as pd
import tensorflow as tf

# Load trained model
model = tf.keras.models.load_model("plant_disease_model.h5")

# Load disease CSV
disease_df = pd.read_csv("disease_info.csv", encoding="latin1")
disease_info = disease_df.set_index("index").to_dict(orient="index")

def predict_disease(img_path):
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
result = predict_disease("testimage.jpg")
print(result)
