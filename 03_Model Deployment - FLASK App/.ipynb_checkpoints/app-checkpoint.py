import numpy as np 
import os

import cv2
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

from keras.models import Sequential
from keras.layers import Conv2D, MaxPool2D, Flatten, Dense

from keras.preprocessing.image import ImageDataGenerator

from keras.callbacks import ModelCheckpoint
import tensorflow as tf
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.models import Model 
from tensorflow.keras.layers import GlobalAveragePooling2D, Input, Dense, concatenate
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import MeanSquaredError
from tensorflow.keras.callbacks import ModelCheckpoint

from flask import Flask, render_template, request, redirect, url_for
import json
import ngrok

from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
import io
import numpy as np




IMG_WIDTH = 224
IMG_HEIGHT = 224
NUM_CHANNELS = 3   
NUM_CLASSES = 2


### MODEL LAYERS & WEIGHTS LOADING ###

base_model_mobile = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
base_model_desktop = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

x_mobile = base_model_mobile.output
x_mobile = GlobalAveragePooling2D()(x_mobile)

x_desktop = base_model_desktop.output
x_desktop = GlobalAveragePooling2D()(x_desktop)

# Add a fully-connected layer
x_mobile = Dense(1024, activation='relu')(x_mobile)
x_desktop = Dense(1024, activation='relu')(x_desktop)

# Add a logistic layer -- we have 1 class
predictions_mobile = Dense(1, activation='sigmoid')(x_mobile)
predictions_desktop = Dense(1, activation='sigmoid')(x_desktop)

model_mobile = Model(inputs=base_model_mobile.input, outputs=predictions_mobile)
model_desktop = Model(inputs=base_model_desktop.input, outputs=predictions_desktop)


for layer in base_model_mobile.layers:
    layer.trainable = False
for layer in base_model_desktop.layers:
    layer.trainable = False

# Compiling models and adding Optimizers

model_mobile.compile(optimizer=Adam(learning_rate=0.001), loss=MeanSquaredError())
model_desktop.compile(optimizer=Adam(learning_rate=0.001), loss=MeanSquaredError())


######### Loading trained weights #############

model_mobile.load_weights("best_weights_MOBILE.h5")
model_desktop.load_weights("best_weights_DESKTOP.h5")


def load_data(direc):
    imgs = []
    for file in os.listdir(direc):
        path = os.path.join(direc, file)
        img = cv2.imread(path)
        img = cv2.resize(img, (IMG_WIDTH, IMG_HEIGHT)) ###############
        imgs.append(img)
    return imgs

def preprocess_data(img_data):
    img_data = np.array(img_data)
    img_data = img_data.astype('float32')
    img_data /= 255.0
    return img_data

def prediction(img):
    img = np.expand_dims(img, axis=0)
    # conv_output = model_mobile(img, training=False)
    predicted = model_mobile.predict(img)

    return predicted



def fetch_test(url):
    opt = webdriver.ChromeOptions()

    # Initialize Selenium Driver
    driver = webdriver.Chrome(options=opt)

    # Open the URL
    driver.get(url)

    # Take screenshot and get the binary data
    screenshot = driver.get_screenshot_as_png()

    # Close the driver
    driver.quit()

    # Use BytesIO to create a file-like object in memory
    # screenshot_stream = io.BytesIO(screenshot)

    # Open the stream as an image with PIL
    # image = Image.open(screenshot_stream)
    img = cv2.imread(screenshot)
    img = cv2.resize(img, (IMG_WIDTH, IMG_HEIGHT))
    img = preprocess_data(img)

    # Convert image to NumPy array
    # image_np = np.array(image)

    # image_list = image_np.tolist()
    return img
    # return image_np



############# Flask Application #############  

app = Flask(__name__)



@app.route('/')
def hello():
    print('http://127.0.0.1:5000/')
    return "server running..."


@app.route('/ping')
def pingPong():
    data = {'mg': "pong"}
    return data  
    
@app.route('/test', methods=['POST'])
def testing():
    data = json.loads(request.get_data())
    print(data, '\n data recieved... pinged \n')
    return json.dumps({'message' : 0, 'hey': 1})

@app.route('/test-it-up', methods=['POST'])
def ui_tester():
    byte_encode = request.get_data()
    print(byte_encode)
    url = byte_encode.decode('utf-8')
    print(url)
    img_preprocessed_data = fetch_test(url)
    # print(list(data.shape))
    

    final_ui_rating = prediction(img_preprocessed_data)
    final_ui_rating_list = final_ui_rating.toList()

       
    return jsonify({"Rating": final_ui_rating_list})
    


if __name__ == '__main__':
    # ngrok.connect(9000, authtoken_from_env=True)
    # print(tunnel.url())
    app.run()











