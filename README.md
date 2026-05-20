# AI Powered Employee Salary Prediction Dashboard

A machine learning based web application that predicts employee salary using employee details such as experience, age, and gender. The project includes a modern dashboard interface, analytics visualizations, and a Flask-based prediction system.

## Features

- Employee salary prediction using Machine Learning
- Interactive dashboard interface
- Salary analytics charts
- Gender distribution visualization
- Modern responsive UI
- Flask backend integration
- Trained ML model using Scikit-learn

## Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- HTML
- CSS
- Bootstrap
- Chart.js
- Gunicorn
- Render

## Machine Learning Model

The project uses a Random Forest Regressor model to predict employee salary based on:

- Experience Years
- Age
- Gender

## Project Structure

```text
employee-salary-prediction/
│
├── app.py
├── train_model.py
├── requirements.txt
├── Procfile
├── runtime.txt
│
├── data/
│   └── employee_data.csv
│
├── model/
│   └── salary_model.pkl
│
├── static/
│   └── styles.css
│
├── templates/
│   └── index.html


# How to Run Locally
Clone the repository
git clone https://github.com/Gudimetlapavani/employee-salary-prediction.git
Open project folder
cd employee-salary-prediction
Install dependencies
pip install -r requirements.txt
Train the model
python train_model.py
Run the Flask app
python app.py
Open browser
http://127.0.0.1:5000
Deployment

This project is deployed using Render.

Resume Description

Developed an AI-powered Employee Salary Prediction Dashboard using Machine Learning and Flask. Implemented data preprocessing, model training, salary prediction, and interactive analytics visualization using Chart.js with a modern responsive UI.

Future Enhancements
Add larger real-world salary dataset
Improve model accuracy
Add login authentication
Add downloadable prediction reports
Add employee data management system
Deploy with database support
Author

Gudimetla Pavani


## 3️⃣ Push README to GitHub

Run:

```bash
git add README.md
git commit -m "Add project README"
git push
