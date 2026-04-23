
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from src.model import model 

app=FastAPI()

class UserInput(BaseModel):
    age:int
    salary:int

@app.get("/")
def home():
    return{"message":"ML API Running"}

@app.post("/predict")
def predict(data:UserInput):
    input_data=np.array([[data.age,data.salary]])
    prediction=model.predict(input_data)


    return{
           "age":data.age,
           "salary":data.salary,
           "prediction":int(prediction[0])
    }