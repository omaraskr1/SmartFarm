# from imp import load_module
import joblib
import numpy as np
import pandas as pd
import cv2
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.models import load_model
class VGG16:
    def __init__(self):
        path_to_artifacts = "../../research/"
        
        self.model = load_model(path_to_artifacts + "VGG16_model1.h5")

   
    from tensorflow import keras

    
    def load_image(self,filename):
        # load the image
        from tensorflow.keras.preprocessing.image import load_img, img_to_array
        img = load_img(filename, target_size=(224, 224))
        # convert to array
        img = img_to_array(img)
        # reshape into a single sample with 3 channels
        img = img.reshape(1, 224, 224, 3)
        # center pixel data
        img = img.astype('float32')
        img = img - [123.68, 116.779, 103.939]
        return img


    def predict(self, img):
        return self.model.predict(img)

   
   
    def postprocessing(self, result):
        # data_dir = 'D:/gp project/plant disess/New Plant Diseases Dataset(Augmented)/New Plant Diseases Dataset(Augmented)'
        # train_dir = data_dir + "/train"
        # train_datagen= ImageDataGenerator()
        # train= train_datagen.flow_from_directory(train_dir,batch_size=128,target_size=(200,200),color_mode='rgb',class_mode='categorical',seed=42)
        # target_names=train.class_indices
        # target_list = list(target_names.items())
        target_list=[('Apple___Apple_scab', 0), ('Apple___Black_rot', 1), ('Apple___Cedar_apple_rust', 2), ('Apple___healthy', 3), ('Blueberry___healthy', 4), ('Cherry_(including_sour)___Powdery_mildew', 5), ('Cherry_(including_sour)___healthy', 6), ('Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 7), ('Corn_(maize)___Common_rust_', 8), ('Corn_(maize)___Northern_Leaf_Blight', 9), ('Corn_(maize)___healthy', 10), ('Grape___Black_rot', 11), ('Grape___Esca_(Black_Measles)', 12), ('Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 13), ('Grape___healthy', 14), ('Orange___Haunglongbing_(Citrus_greening)', 15), ('Peach___Bacterial_spot', 16), ('Peach___healthy', 17), ('Pepper,_bell___Bacterial_spot', 18), ('Pepper,_bell___healthy', 19), ('Potato___Early_blight', 20), ('Potato___Late_blight', 21), ('Potato___healthy', 22), ('Raspberry___healthy', 23), ('Soybean___healthy', 24), ('Squash___Powdery_mildew', 25), ('Strawberry___Leaf_scorch', 26), ('Strawberry___healthy', 27), ('Tomato___Bacterial_spot', 28), ('Tomato___Early_blight', 29), ('Tomato___Late_blight', 30), ('Tomato___Leaf_Mold', 31), ('Tomato___Septoria_leaf_spot', 32), ('Tomato___Spider_mites Two-spotted_spider_mite', 33), ('Tomato___Target_Spot', 34), ('Tomato___Tomato_Yellow_Leaf_Curl_Virus', 35), ('Tomato___Tomato_mosaic_virus', 36), ('Tomato___healthy', 37)]

        # result = self.model.predict(img)
        result = target_list[np.argmax(result)]
       
        return { "label": result, "status": "OK"}

    def compute_prediction(self, img):
        try:
            load_img = self.load_image(img)
            prediction = self.predict(load_img)  # only one sample
            prediction = self.postprocessing(prediction)
        except Exception as e:
            return {"status": "Error", "message": str(e)}

        return prediction