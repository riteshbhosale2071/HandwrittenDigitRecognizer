# 🧠 Handwritten Digit Recognizer

An end-to-end Machine Learning project that trains a Convolutional
Neural Network (CNN) on the MNIST dataset and deploys it using a
Tkinter-based desktop GUI for real-time digit prediction.

------------------------------------------------------------------------

## 🚀 Features

-   Train CNN model on MNIST dataset
-   Evaluate model accuracy
-   Save and load trained model
-   Desktop GUI using Tkinter
-   Select external digit images for prediction
-   Clean project structure
-   Model path handling using dynamic paths

------------------------------------------------------------------------

## 🏗 Project Structure

    HandwrittenDigitRecognizer/
    │
    ├── models/
    │   └── digit_model.keras
    │
    ├── data/
    │   └── mnist_images/
    │
    ├── notebook/
    │   └── main.py
    │
    ├── app.py
    │
    ├── requirements.txt
    ├── README.md
    └── .gitignore

------------------------------------------------------------------------

## 🛠 Tech Stack

-   Python
-   TensorFlow / Keras
-   NumPy
-   Pillow (PIL)
-   Tkinter (GUI)
-   Matplotlib (debug visualization)

------------------------------------------------------------------------

## ⚙️ Installation Guide

### 1️⃣ Download or Clone the Repository

``` bash
git clone https://github.com/riteshbhosale2071/HandwrittenDigitRecognizer.git
cd HandwrittenDigitRecognizer
```

Or download ZIP directly from GitHub and extract it.

------------------------------------------------------------------------

### 2️⃣ Create Virtual Environment (Recommended)

``` bash
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # Mac/Linux
```

------------------------------------------------------------------------

### 3️⃣ Install Dependencies

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

### 4️⃣ Train the Model

``` bash
python notebook/main.py
```

This will: - Download MNIST dataset - Train CNN model - Save trained
model to:

    models/digit_model.keras

------------------------------------------------------------------------

### 5️⃣ Set Dataset Folder Path in GUI (Important)

Open:

    app.py

Find this section:

``` python
model = tf.keras.models.load_model("File Path")
```

If your dataset is stored elsewhere, update `File Path` to your dataset
path:

Example:

``` python
model = tf.keras.models.load_model("C:/YourFolder/mnist_images")
```

------------------------------------------------------------------------

## ▶️ Run the Application

``` bash
python app.py
```

Steps: 1. Click **Choose Image** 2. Select a digit image 3. View
predicted digit in GUI

------------------------------------------------------------------------

## 🎯 Model Performance

-   Achieves \~97%--99% accuracy on MNIST test dataset

------------------------------------------------------------------------

## 📌 Future Improvements

-   Add draw-with-mouse feature
-   Add probability bar visualization
-   Convert to web application
-   Export as executable (.exe)
-   Add webcam-based digit detection

------------------------------------------------------------------------

## 👨‍💻 Author

Ritesh Bhosale

------------------------------------------------------------------------

⭐ If you found this project useful, consider giving it a star on
GitHub!