from fastapi import FastAPI
from pydantic import BaseModel
from src.predict import predict_student

app=FastAPI()

class StudentInput(BaseModel):
    hours:int
    attendance:int
    previous_marks:int
    sleep:int

@app.get("/")    
def home():
    return{"message":"student performance API"}

@app.post("/predict")
def predict(data:StudentInput):


    prediction,confidence=predict_student(
        data.hours,
        data.attendance,
        data.previous_marks,
        data.sleep
    )

    return{
        "prediction":prediction,
        "confidence":confidence
    }

