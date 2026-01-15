# Kaggle Titanic Survival Predictor

A Flask-based web application that predicts whether a passenger would survive the Titanic disaster using machine learning.

## Overview

This is a simple classification project using a Logistic Regression model trained on the Kaggle Titanic dataset. The main purpose of this project is to learn how to deploy a machine learning model as an API and build a basic interface to interact with it, rather than to achieve high model performance.

## Objective

**Build a prediction API using Flask
**Create a simple HTML template to provide a user-friendly interface for interacting with the API
**Use scikit-learn pipelines and preprocessing transformers to build a single end-to-end workflow (preprocessing + model) that directly outputs predictions.
## Project Structure

```
Kaggle-Titanic/
├── app.py                    # Flask application
├── model.pkl                 # Trained logistic regression model
├── custom_transform.py       # Feature engineering function
├── notebook.ipynb            # Jupyter notebook with model training
├── train.csv                 # Training dataset
├── templates/
│   └── home.html            # Web interface template
└── README.md
```

### Web Interface

1. **Start the Flask app:**
   ```bash
   python app.py
   ```

2. **Open your browser and go to:**
   ```
   http://localhost:5000
   ```

3. **Fill in the passenger details and click "Predict"** to see survival prediction (alive/dead)


## Performance

The model achieves approximately **80%+ accuracy** on the test set (based on standard Titanic dataset splits).

## Dependencies

- Flask
- NumPy
- Pandas
- scikit-learn

