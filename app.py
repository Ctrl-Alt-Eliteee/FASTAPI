from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from  src.predict import predict_student

app=FastAPI()

class StudentInput(BaseModel):
    hours: int
    attendance:int
    previous_marks:int

@app.get("/")
def home():
    return{"message":"Student Performance API"}

@app.post("/predict")
def predict(data:StudentInput):
    result=predict_student(
        data.hours,
        data.attendance,
        data.previous_marks
    )


    return{"prediction":result}