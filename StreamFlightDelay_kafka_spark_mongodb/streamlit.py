import time
import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

st.title('Flight Analysis')
image = Image.open("/home/preeti/title.jpeg")
st.image(image,width=700)

rad = st.sidebar.radio("Navigation", ("Architecture", "Predictions", "Dataset"))
if rad == "Architecture":
    st.title("Architecture of Project")
    st.graphviz_chart("""
    digraph {
        KAFKA -> SPARK
        SPARK -> MONGODB1
        MONGODB1 -> FlightAnalysis
        FlightAnalysis -> SPARK
        SPARK -> MONGODB2
        MONGODB2 -> DASHBOARD
        }
    """)

elif rad == "Predictions":
    st.title("Flight Predictions")
    st.sidebar.header("Regression")
    pre = st.sidebar.selectbox("Select a number", ["Linear Regression","Logistic Regression"])
    if pre == "Linear Regression":
        st.header("Linear Regression")
        st.subheader("!!Prediction using Linear Regression!!")
        progress = st.progress(0)
        for i in range(100):
            time.sleep(0.1)
            progress.progress(i+1)
        st.balloons()
        db = client["result"]
        collection = db["score"]
        data = list(collection.find({}, projection={"_id": False}))
        st.header('')
        st.table(data)
    elif pre == "Logistic Regression":
        st.header("Logistic Regression")
        st.subheader("!!Prediction using Logistic Regression!!")
        progress = st.progress(0)
        for i in range(100):
            time.sleep(0.1)
            progress.progress(i+1)
        st.balloons()
        db = client["flight"]
        collection = db["logistic"]
        data = list(collection.find({"prediction":1},{"_id":1,"origin":1,"dest":1}))
        st.header('')
        st.table(data)

elif rad == "Dataset":
    st.title("Dataset")
    st.header("The dataset used for the project is:")
    db = client["project"]
    collection = db["bigdata"]
    data = list(collection.find({}, projection={"_id": False}))
    st.header('')
    st.table(data)
