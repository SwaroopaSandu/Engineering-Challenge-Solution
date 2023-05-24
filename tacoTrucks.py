#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv("Mobile_Food_Facility_Permit.csv")


# In[3]:


df


# In[5]:


##Dropping the missing values

def get_taco_trucks():
    df = pd.read_csv("Mobile_Food_Facility_Permit.csv")
    
    # Drop rows with missing values in the "FoodItems" column
    df = df.dropna(subset=["FoodItems"])
    
    # Filter the dataset to include only taco trucks
    taco_trucks = df[df["FoodItems"].str.contains("taco", case=False)]
    
    # Extract the names of taco trucks
    taco_truck_names = taco_trucks["Applicant"].tolist()
    return taco_truck_names

if __name__ == "__main__":
    taco_trucks = get_taco_trucks()
    for truck in taco_trucks:
        print(truck)


# In[ ]:
from flask import Flask, jsonify
from flask_cors import CORS

import pandas as pd

app = Flask(__name__)
CORS(app)

@app.route('/foodtrucks', methods=['GET'])
def get_food_trucks():
    df = pd.read_csv("Mobile_Food_Facility_Permit.csv")
   
    df = df.dropna(subset=["FoodItems"])
    taco_trucks = df[df["FoodItems"].str.contains("tacos", case=False)]
    truck_names = taco_trucks["Applicant"].tolist()
    print(len(truck_names))
    return jsonify(truck_names)

if __name__ == '__main__':
    app.run(debug=True)




