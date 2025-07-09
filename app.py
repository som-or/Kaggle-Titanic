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

@app.route('/predict', methods=['POST'])
def predict():
    data=[request.form.values()]
    data = pd.DataFrame(data, columns=['PassengerId', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin','Embarked'])
    prediction = model.predict(data)[0].item()
    output = 'dead' if prediction == 1 else 'alive'
    print(output)
    return render_template('home.html', prediction_text='The Passenger is {}'.format(output))

if __name__== "__main__":
    app.run(debug=True)