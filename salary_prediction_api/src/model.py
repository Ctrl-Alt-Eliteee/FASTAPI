import numpy as np
from sklearn.tree import DecisionTreeClassifier

x=np.array([[18,15000],
            [22,20000],
            [35,40000],
            [45,60000],
            [50,800000]])
y=np.array([0,0,1,1,1])

model=DecisionTreeClassifier()
model.fit(x,y)