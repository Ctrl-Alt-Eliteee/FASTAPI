import streamlit as st
import requests
st.title("STUDENT PERFORMANCE PREDICTOR")

hours=st.slider("Hours studied",0,10,5)
attendance=st.slider("Attendance(%)",0,100,75)
previous_marks=st.slider("Previous Marks",0,100,50)

if st.button("predict"):

    url="http://127.0.0.1:8000/predict"

    data={
        "hours":hours,
        "attendance":attendance,
        "previous_marks":previous_marks
    }

    response = requests.post(url, json=data)

    result = response.json()

    if result["prediction"] == 1:
        st.success("✅ Student will PASS")
    else:
        st.error("❌ Student will FAIL")