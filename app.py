import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# LOAD MODEL
model = tf.keras.models.load_model("digit_model.keras")
print("Model loaded!")

# PREPROCESS
def preprocess_image(path):
    img = Image.open(path).convert("L")
    img = np.array(img).astype("float32")

    img = img / 255.0
    img = img.reshape(1, 28, 28, 1)
    return img

# CHOOSE IMAGE
def choose_image():
    file_path = filedialog.askopenfilename(
        initialdir="mnist_images",
        filetypes=[("Image files", "*.png")]
    )

    if not file_path:
        return

    # show selected image
    show_img = Image.open(file_path).resize((150,150))
    img_tk = ImageTk.PhotoImage(show_img)
    image_label.config(image=img_tk)
    image_label.image = img_tk

    # preprocess
    processed = preprocess_image(file_path)

    # debug view
    plt.imshow(processed.reshape(28,28), cmap="gray")
    plt.title("Given to model")
    plt.show()

    # predict
    pred = model.predict(processed)
    digit = np.argmax(pred)

    print("Probabilities:", pred)
    result_label.config(text=f"Predicted: {digit}")

# GUI
root = tk.Tk()
root.title("Digit Recognizer")
root.geometry("350x450")

tk.Label(root, text="MNIST Digit Recognizer", font=("Arial",16)).pack(pady=10)

image_label = tk.Label(root)
image_label.pack(pady=10)

tk.Button(root, text="Choose Image", command=choose_image).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial",18))
result_label.pack(pady=20)

root.mainloop()