import numpy as np

car_class = {0:"Audi", 1:"Hyundai Creta", 2:"Mahindra Scorpio", 3:"Rolls Royce",
             4:"Swift", 5:"Tata Safari", 6:"Toyota Innova"}

def predict_car_brand(model, hog):
    brand = model.predict(np.array([hog["HOG"]]))
    return {"Brand":car_class[brand[0]]}