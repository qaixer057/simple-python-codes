#for saving a model at particular location
target_dir = './models/'
if not os.path.exists(target_dir):
  os.mkdir(target_dir)
model.save('./models/MelanomaModel.h5')
model.save_weights('./models/MelanomaWeights.h5')


#for loading trained CNN model
import os
import numpy as np
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import Sequential, load_model

img_width, img_height = 224, 224
model_path = './models/MelanomaModel.h5'
model_weights_path = './models/MelanomaWeights.h5'
model = load_model(model_path)
model.load_weights(model_weights_path)
