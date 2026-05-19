from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open('model/salary_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    experience = float(request.form['experience'])
    age = float(request.form['age'])
    gender = request.form['gender']

    # Convert gender
    gender = 1 if gender == 'Male' else 0

    # Create feature array
    features = np.array([[experience, age, gender]])

    # Predict salary
    prediction = model.predict(features)

    return render_template(
        'index.html',
        prediction_text=f'Predicted Salary: ₹ {prediction[0]:,.2f}'
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)