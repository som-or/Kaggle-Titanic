import pickle
from flask import Flask, request, app, jsonify, render_template, url_for
import numpy as np
import pandas as pd

from custom_transform import custom_transform

app=Flask(__name__)
#load the model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data= request.json['data']
    print(data)
    # Convert the JSON data to a DataFrame
    cols =['PassengerId', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin','Embarked']
    data = pd.DataFrame(data, index=[0], columns=cols)
    prediction = model.predict(data)
    output = prediction[0].item()
    print(output)
    return jsonify({ 'prediction': output })


if __name__== "__main__":
    app.run(debug=True)