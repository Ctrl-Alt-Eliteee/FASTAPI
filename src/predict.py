import joblib
import numpy as np

model=joblib.load("src/model.pkl")

def predict_student(hours,attendance,previous_marks):
    data=np.array([[hours,attendance,previous_marks]])
    prediction=model.predict(data)
    return int(prediction[0])