#REAL-TIME FLIGHT DELAY AND DISTANCE PREDICTION
-------------------------------------------------

PROJECT OVERVIEW:
This project demonstrates a real-time big data pipeline that predicts flight delays and distances using Apache Kafka, Spark Streaming, MongoDB, and Streamlit.
It integrates both classification (Logistic Regression) and regression (Linear Regression) models to perform predictive analysis on live flight datasets.

The system was built as part of the 21AIE304 - Big Data and Database Management course at Amrita School of Engineering, Bangalore.

-------------------------------------------------
ARCHITECTURE:
Kafka  →  Spark Streaming  →  MongoDB  →  Streamlit Dashboard

COMPONENTS:
1. Kafka Producer (Python): Streams flight data from JSON files.
2. Spark / PySpark: Performs machine learning (Logistic and Linear Regression).
3. MongoDB: Stores both the raw and processed data.
4. Streamlit: Displays the analysis results and dataset visually.

-------------------------------------------------
DATA DESCRIPTION:
Dataset Source: Bureau of Transportation Statistics (Real-time flight data)

Features include:
- id: Unique flight ID (carrier + date + origin + destination + flight number)
- dofW: Day of the week
- carrier: Airline code
- origin: Origin airport
- dest: Destination airport
- crsdephour: Scheduled departure hour
- crsdeptime: Scheduled departure time
- depdelay: Departure delay in minutes
- crsarrtime: Scheduled arrival time
- arrdelay: Arrival delay in minutes
- crselapsedtime: Elapsed time of flight
- dist: Distance between source and destination

-------------------------------------------------
PROCESS FLOW:

1. PRODUCER (Producer.py):
   - Reads flight data from JSON files.
   - Publishes messages to Kafka topic “god” at fixed intervals.
   - Each message contains cleaned flight information.

2. LINEAR REGRESSION (Python / PySpark):
   - Reads streaming data from Kafka.
   - Stores data into MongoDB collection “project.bigdata”.
   - Uses PySpark MLlib Linear Regression to predict flight distance (‘dist’).
   - Predictions are written into MongoDB collection “result.score”.

3. LOGISTIC REGRESSION (Scala / Spark):
   - Classifies flights as delayed or on-time.
   - Data is bucketized based on ‘depdelay’ using Bucketizer.
   - Categorical features are encoded using StringIndexer and OneHotEncoder.
   - Logistic Regression model trained with cross-validation.
   - Predictions streamed to MongoDB collection “flight.logistic”.

4. MONGODB:
   - Acts as persistent storage for all raw and processed data.
   - Database Names: project, result, flight
   - Collections: bigdata, score, logistic

5. STREAMLIT DASHBOARD (streamlit.py):
   - Connects to MongoDB.
   - Displays three sections:
        a) Architecture: Graph of data flow.
        b) Predictions: Displays Linear and Logistic Regression results.
        c) Dataset: Shows raw flight data.
   - Runs locally on port 8501.

-------------------------------------------------
HOW TO RUN:

1. Start Zookeeper and Kafka servers:
   bin/zookeeper-server-start.sh config/zookeeper.properties
   bin/kafka-server-start.sh config/server.properties

2. Create a Kafka topic:
   bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --topic god --partitions 1 --replication-factor 1

3. Run the Kafka Producer:
   python3 Producer.py

4. Start Spark Streaming (choose one mode):
   - For Linear Regression:
       bin/pyspark --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.1
   - For Logistic Regression:
       ./bin/spark-shell --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.1,org.mongodb.spark:mongo-spark-connector_2.12:10.1.0

5. Start MongoDB service:
   sudo systemctl start mongod

6. Run Streamlit Dashboard:
   streamlit run streamlit.py
   Access at: http://localhost:8501/

-------------------------------------------------
RESULTS:
- Logistic Regression classifies whether a flight is delayed or not.
- Linear Regression predicts flight distance.
- Results are displayed in Streamlit from MongoDB collections.

Example MongoDB Queries:
   use flight
   db.logistic.find({"prediction":1},{"_id":1,"origin":1,"dest":1})

-------------------------------------------------
TOOLS AND TECHNOLOGIES:
- Python, Scala
- Apache Kafka
- Apache Spark (Streaming, MLlib)
- MongoDB (NoSQL database)
- Streamlit (Dashboard UI)
- Pandas, NumPy, Matplotlib

-------------------------------------------------
TEAM MEMBERS:
- Hema Srivarshini Chilakala (BL.EN.U4AIE20019)
- N. Preeti (BL.EN.U4AIE20037)
- Sreekar Praneeth Marri (BL.EN.U4AIE20061)

Department of CSE, Amrita School of Engineering, Bangalore
-------------------------------------------------
