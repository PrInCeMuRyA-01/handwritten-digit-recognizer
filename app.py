import base64
import io
import os

import numpy as np
from flask import Flask, jsonify, request, send_from_directory
from PIL import Image
from tensorflow.keras.models import load_model

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "digit_cnn.keras")

app = Flask(__name__, static_folder=BASE_DIR, static_url_path="")
model = None


def get_model():
    global model
    if model is None and os.path.exists(MODEL_PATH):
        model = load_model(MODEL_PATH)
    return model


@app.get("/")
def home():
    return send_from_directory(BASE_DIR, "index.html")


@app.post("/predict")
def predict():
    active_model = get_model()
    if active_model is None:
        return jsonify({
            "error": "Model file not found. Run `python train_model.py` first."
        }), 503

    payload = request.get_json(silent=True) or {}
    image_data = payload.get("image", "")
    if not image_data or "," not in image_data:
        return jsonify({"error": "Please draw a digit before predicting."}), 400

    try:
        raw = base64.b64decode(image_data.split(",", 1)[1])
        image = Image.open(io.BytesIO(raw)).convert("RGB")
        # The canvas and MNIST both use a black background with a bright digit.
        image = ImageOps.grayscale(image)
        image = image.resize((28, 28), Image.Resampling.LANCZOS)
        array = np.asarray(image, dtype=np.float32) / 255.0
        array = array.reshape(1, 28, 28, 1)

        probabilities = active_model.predict(array, verbose=0)[0]
        digit = int(np.argmax(probabilities))
        confidence = float(probabilities[digit]) * 100
        return jsonify({"digit": digit, "confidence": f"{confidence:.2f}%"})
    except Exception as exc:
        app.logger.exception("Prediction failed")
        return jsonify({"error": f"Could not process image: {exc}"}), 400


if __name__ == "__main__":
    if not os.path.exists(MODEL_PATH):
        print("Model missing. Run `python train_model.py` before starting the app.")
    app.run(debug=True)
