# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 00:57:37 2023

@author: hp
"""

from flask import Flask, render_template, request
import pandas as pd
import pickle

model = pickle.load(open('model.pkl','rb'))
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/details')
def pred():
    return render_template('predict.html')

@app.route('/predict',methods = ['GET','POST'])
def predict():
    SIZE = request.form['SIZE']
    FUEL = request.form['FUEL']
    DISTANCE = request.form['DISTANCE']
    DESIBEL = request.form['DESIBEL']
    AIRFLOW = request.form['AIRFLOW']
    FREQUENCY = request.form['FREQUENCY']
        
    total = [[SIZE,FUEL,DISTANCE,DESIBEL,AIRFLOW,FREQUENCY]]
    d1 = pd.DataFrame(data = total, columns = ['SIZE','FUEL','DISTANCE','DESIBEL','AIRFLOW','FREQUENCY'])
    prediction = model.predict(d1)
    prediction = prediction[0]
    if prediction == 0:
        return render_template('results.html', prediction_text = "The fire is in non extinction state")
    else:
        return render_template('results.html', prediction_text = "The fire is in extinction state.")
    
if __name__ == "__main__":
    app.run(debug= True)