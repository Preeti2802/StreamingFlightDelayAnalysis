# ✈️ REAL-TIME FLIGHT DELAY AND DISTANCE PREDICTION
---
## PROJECT OVERVIEW
This project demonstrates a real-time Big Data pipeline that predicts **flight delays** and **flight distances** using  
**Apache Kafka**, **Apache Spark Streaming**, **MongoDB**, and **Streamlit**.  

It integrates both:
- **Classification (Logistic Regression)** – to predict if a flight is delayed or on-time  
- **Regression (Linear Regression)** – to predict the flight distance  

## 🏗️ ARCHITECTURE OVERVIEW

### Data Flow & Components
1. **Kafka Producer (Python):** Streams flight data from JSON files into Kafka topics.  
2. **Spark / PySpark:** Performs machine learning using Linear & Logistic Regression.  
3. **MongoDB:** Stores both raw and processed data.  
4. **Streamlit:** Displays the analysis results and dataset visually.  

