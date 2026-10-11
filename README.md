# Handwritten Digit Recognizer (CNN)

A small web app that lets you draw a digit (0–9) and predicts it with a Convolutional Neural Network (CNN). The frontend uses HTML, CSS, and JavaScript; the backend uses Flask and TensorFlow/Keras.

## Project structure

```text
handwritten-digit-recognizer/
├── app.py
├── train_model.py
├── requirements.txt
├── index.html
├── style.css
├── script.js
├── CNN(Deep_Learning).ipynb
├── .gitignore
└── README.md
```

## Run locally

Python 3.10 or 3.11 is recommended for compatibility with TensorFlow.

1. Open a terminal in this project folder.
2. Create and activate a virtual environment:

   **Windows**
   ```bash
   py -m venv .venv
   .venv\\Scripts\\activate
   ```

   **macOS/Linux**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install packages:
   ```bash
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```
4. Train the CNN and create the local model file:
   ```bash
   python train_model.py
   ```
   The first run downloads MNIST data and can take a while. The generated `digit_cnn.keras` file is excluded from Git by `.gitignore`; users can recreate it by running this command.
5. Start the website:
   ```bash
   python app.py
   ```
6. Open http://127.0.0.1:5000 in your browser.

## Upload to GitHub

1. Create a new empty repository on GitHub, for example `handwritten-digit-recognizer`.
2. Extract this project ZIP.
3. In a terminal, `cd` into the extracted project folder and run:

   ```bash
   git init
   git add .
   git commit -m "Add CNN handwritten digit recognizer"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/handwritten-digit-recognizer.git
   git push -u origin main
   ```

   Replace `YOUR-USERNAME` with your GitHub username. If Git asks you to sign in, complete GitHub authentication.

## Important notes

- GitHub stores your code; it does not automatically run the Flask app.
- The app needs the Python backend and a trained model. A static-only host such as GitHub Pages cannot run this Flask/TensorFlow backend.
- To make it publicly usable, deploy the Python app to a host that supports Flask and TensorFlow, then share that hosted URL.
- The notebook you supplied is included as a reference. The included `train_model.py` is a standalone training script and uses TensorFlow's MNIST dataset, so it does not require separate `train.csv` or `test.csv` files.
