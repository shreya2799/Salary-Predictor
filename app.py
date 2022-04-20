# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 11:40:21 2022

@author: juhig
"""


import numpy as np
import pickle
from flask import Flask,request,render_template

app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI

    Returns
    -------
    None.

    '''
    int_features=[int(x) for x in request.form.values()]
    final_features=[np.array(int_features)]
    prediction=model.predict(final_features)
    
    output=round(prediction[0],2)
    
    return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))


if __name__=="__main__":
    app.run(debug=True)
    