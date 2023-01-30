#!/bin/python3 
import pandas as pd 
import numpy as np 
from kafka import KafkaProducer 
from kafka.producer import KafkaProducer 
from time import sleep 
producer = KafkaProducer(bootstrap_servers=["localhost:9092"],key_serializer=str.encode,value_serializer=str.encode) 
df = pd.read_json('/home/preeti/flightdelay/data/flights20170304.json',lines=True) 
for row in df.values: 
 temp = np.ndarray.tolist(row) 
 temp_str = str(temp).replace("[","").replace("]","").replace('"',"").replace("'","") 
 producer.send("god",key="temp",value=temp_str) 
 sleep(3)

