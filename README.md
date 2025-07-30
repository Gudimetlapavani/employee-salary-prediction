# employee-salary-prediction
🧠 Project Prompt: Employee Salary Prediction & Analysis
🎯 Project Title:
Employee Salary Prediction using Machine Learning with Web Interface

📌 Problem Statement:
In modern organizations, determining fair and accurate employee compensation is crucial yet challenging. Manual salary decisions can be inconsistent and biased due to the complexity of factors like education level, experience, and age. This project aims to automate salary prediction using machine learning techniques, ensuring a data-driven and efficient decision-making process. The model is trained on real employee data to predict annual salaries with high accuracy, assisting HR teams and business analysts.

🔧 System Development Approach:
👨‍💻 Backend:
Language: Python

Libraries Used:

pandas for data handling

scikit-learn for machine learning (e.g., Linear Regression, KNN)

pickle for saving the trained model

Flask for backend web integration

🎨 Frontend:
HTML for form structure

CSS for styling

Form input includes: education level, years of experience, and age

📁 Folder Structure:
cpp
Copy
Edit
employee-salary-prediction/
├── app.py
├── model/
│   └── salary_model.pkl
├── data/
│   └── employee_data.csv
├── templates/
│   └── index.html
├── static/
│   └── styles.css
├── requirements.txt
└── README.md
📈 Algorithm and Deployment – Step-by-Step:
Data Preprocessing:

Load the dataset (employee_data.csv)

Select key features: education level, experience, and age

Clean and normalize the data

Model Training:

Use Linear Regression to fit the data

Optionally compare with KNN (based on your uploaded notebook)

Save trained model to salary_model.pkl using pickle

Web Application:

Flask is used to build a backend API

Frontend (HTML + CSS) form takes user inputs

Inputs are passed to the model, and prediction is displayed

Prediction Output:

The predicted monthly salary is multiplied by 12

Final result: Predicted Annual Salary (in ₹)
