import numpy as np
import streamlit as st
from ultralytics import YOLO
from keras.utils import load_img

def run_app():
    st.title("Brain Tumor Detection")
    image = st.file_uploader(label="Choose an MRI image of the brain for segmentation", type=["jpg", "png"])

    if image is not None:
        model_1 = YOLO("best.pt")
        prediction = model_1(load_img(image, target_size=(640, 640)), imgsz=224, conf=0.5)[0]
        tumor_cls =prediction.names # Get the class name
        pred_index = np.argmax(prediction.probs.data).item() # get the class index
        prediction = tumor_cls[pred_index] # Get the final prediction
        
        if st.button(label="Click to make Prediction"):
            st.image(load_img(image, target_size=(480, 480)))
            st.markdown(body=f"Prediction: {prediction}")

if __name__ == "__main__":
    run_app()
