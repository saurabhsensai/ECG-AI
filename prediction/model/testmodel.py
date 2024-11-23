from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

import numpy as np

# Load the model
model_path = "C://Users//saurabh nale//Desktop//production//model//alexnet_model.h5"  
loaded_model = load_model(model_path)



img_path = 'C:\Users\saurabh nale\Desktop\ecgsite\prediction\imagegen\testing\1.jpg'  
img = image.load_img(img_path, target_size=(227, 227)) 
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)


predictions = loaded_model.predict(img_array)

return(predictions)


