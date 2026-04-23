import numpy as np
from sklearn.ensemble import RandomForestClassifier
import  joblib

x=np.array([
    [1, 50, 40],
    [2, 60, 45],
    [3, 65, 50],
    [4, 70, 55],
    [5, 75, 60],
    [6, 80, 65],
    [7, 85, 70],
    [8, 90, 75],
    [2, 55, 35],
    [3, 60, 38]
])
y=np.array([0,0,0,1,1,1,1,1,0,0])

model=RandomForestClassifier(n_estimators=20)

model.fit(x,y)

joblib.dump(model,"src/model.pkl")

print("Model saved successfully")