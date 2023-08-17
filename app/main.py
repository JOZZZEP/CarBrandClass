from fastapi import FastAPI, Request
from code import predict_car_brand
import pickle
import os
import requests

app = FastAPI()

#For local
model = pickle.load(open(f'D:\Coding\Leaning\Ai\CarBrandClass\model\carmodel.pkl', 'rb'))
#For docker
# model = pickle.load(open(os.getcwd()+r'model\carmodel.pkl', 'rb'))

endpoint = "http://localhost:5555/api/gethog"

@app.post("/api/carbrand")
async def read_str(data : Request):
    data = await data.json()
    hog = requests.get(endpoint, json=data)
    brand = predict_car_brand(model, hog.json())
    return brand