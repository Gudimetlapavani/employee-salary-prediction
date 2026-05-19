import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import pickle

# Load dataset
df = pd.read_csv('data/employee_data.csv')

# Convert Gender into numeric
le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])

# Features
X = df[['Experience_Years', 'Age', 'Gender']]

# Target
y = df['Salary']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestRegressor()

model.fit(X_train, y_train)

# Save model
pickle.dump(model, open('model/salary_model.pkl', 'wb'))

print("✅ Model trained successfully!")