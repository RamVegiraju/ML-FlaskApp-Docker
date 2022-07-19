from flask import Flask, request, jsonify, render_template, session, redirect, url_for, session
import requests
import pandas as pd
import numpy as np
import pickle
import joblib


model_rf = pickle.load(open('model.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods = ['POST'])
def getvalue():
    taxUser = int(request.form['tax'])
    incomeUser = int(request.form['income'])
    highwaysUser = int(request.form['highways'])
    licenseUser = request.form['license']
    res = model_rf.predict([[taxUser, incomeUser, highwaysUser, licenseUser]])[0]
    print(res)
    print(type(res))
    return render_template('index.html', res = res)

if __name__ =='__main__':
    app.run(debug=True)

