import os
import cv2
from deepface import DeepFace
from mtcnn import MTCNN
import numpy as np

def detect_and_crop_face(image):
    detector = MTCNN()
    detections = detector.detect_faces(image)
    if detections:
        x, y, width, height = detections[0]['box']
        cropped_face = image[y:y+height, x:x+width]
        return cropped_face
    else:
        raise Exception("No face detected in the image")

def preprocess_image(image, target_size=(224, 224)):
    if len(image.shape) == 3 and image.shape[2] == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX)
    image = cv2.resize(image, target_size)
    image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    return image

def verify_face(id_face, live_face):
    id_face_preprocessed = preprocess_image(id_face)
    live_face_preprocessed = preprocess_image(live_face)
    
    temp_id_image_path = 'temp_id_image.jpg'
    temp_live_image_path = 'temp_live_image.jpg'
    
    try:
        cv2.imwrite(temp_id_image_path, id_face_preprocessed)
        cv2.imwrite(temp_live_image_path, live_face_preprocessed)
        
        result = DeepFace.verify(img1_path=temp_id_image_path, img2_path=temp_live_image_path, model_name='ArcFace')
    finally:
        if os.path.exists(temp_id_image_path):
            os.remove(temp_id_image_path)
        if os.path.exists(temp_live_image_path):
            os.remove(temp_live_image_path)
    
    return result



