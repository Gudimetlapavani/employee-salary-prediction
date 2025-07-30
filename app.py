from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle

app = Flask(_name_)

# Load trained model
model = pickle.load(open("model/salary_model.pkl", "rb"))

# Encoding dictionaries (should match training)
position_map = {'Developer': 0, 'Manager': 1, 'Analyst': 2}
education_map = {'Bachelor': 0, 'Master': 1, 'PhD': 2}

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    experience = int(request.form['experience'])
    position = position_map[request.form['position']]
    education = education_map[request.form['education']]

    features = np.array([[experience, position, education]])
    prediction = model.predict(features)

    return render_template('index.html', prediction_text=f'Predicted Salary: ${prediction[0]:,.2f} per year')

if _name_ == '_main_':
    app.run(debug=True)
🧾 templates/index.html (Input Form UI)
<!DOCTYPE html>
<html>
<head>
    <title>Employee Salary Predictor</title>
</head>
<body>
    <h2>Employee Salary Prediction</h2>
    <form method="POST" action="/predict">
        <label>Experience (Years):</label><br>
        <input type="number" name="experience" required><br><br>

        <label>Position:</label><br>
        <select name="position" required>
            <option value="Developer">Developer</option>
            <option value="Manager">Manager</option>
            <option value="Analyst">Analyst</option>
        </select><br><br>

        <label>Education:</label><br>
        <select name="education" required>
            <option value="Bachelor">Bachelor</option>
            <option value="Master">Master</option>
            <option value="PhD">PhD</option>
        </select><br><br>

        <input type="submit" value="Predict Salary">
    </form>

    <h3>{{ prediction_text }}</h3>
</body>
</html>
model_training.py (Train and Save Model)
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset
df = pd.read_csv('data/employee_data.csv')

# Encode categorical columns
df['position'] = df['position'].map({'Developer': 0, 'Manager': 1, 'Analyst': 2})
df['education'] = df['education'].map({'Bachelor': 0, 'Master': 1, 'PhD': 2})

X = df[['experience', 'position', 'education']]
y = df['salary']

# Train model
model = LinearRegression()
model.fit(X, y)
