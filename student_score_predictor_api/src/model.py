import numpy as np
from sklearn.ensemble import RandomForestClassifier
import  joblib
#features:[hours,attendance,previous_marks,sleep_hours]
x=np.array([
     [1, 50, 40, 5],
    [2, 55, 45, 6],
    [3, 60, 50, 6],
    [4, 65, 55, 7],
    [5, 70, 60, 7],
    [6, 75, 65, 7],
    [7, 80, 70, 8],
    [8, 85, 75, 8],
    [2, 50, 35, 5],
    [3, 55, 38, 6],
    [4, 60, 42, 6],
    [5, 65, 48, 7],
    [6, 70, 55, 7],
    [7, 75, 60, 8],
    [8, 80, 68, 8]
])
y=np.array([0,0,0,1,1,1,1,1,0,0,0,1,1,1,1])

model=RandomForestClassifier(n_estimators=60)

model.fit(x,y)

joblib.dump(model,"src/model.pkl")

print("Model saved successfully")