from fastapi import FastAPI, Request
import pickle
import os
import requests
#For docker change to app.code
from app.code import predict_car_brand
app = FastAPI()

#For local
# model = pickle.load(open(f'D:\Coding\Leaning\Ai\CarBrandClass\model\carmodel.pkl', 'rb'))
#For docker
model = pickle.load(open(f'model/carmodel_xgb.pkl', 'rb'))

endpoint = "http://172.17.0.2:80/api/gethog"

@app.post("/api/carbrand")
async def read_str(data : Request):
    data = await data.json()
    hog = requests.get(endpoint, json=data)
    brand = predict_car_brand(model, hog.json())
    return brand