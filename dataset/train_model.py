import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

# Read student dataset
data = pd.read_csv("dataset/students.csv")

# Select input features
X = data[[
    "attendance",
    "study_hours",
    "previous_marks",
    "assignment_score"
]]

# Select target
y = data["performance"]

# Create Machine Learning model
model = DecisionTreeClassifier(random_state=42)

# Train the model
model.fit(X, y)

print("Machine Learning Model Trained Successfully!")

# Test with a sample student
new_student = pd.DataFrame([{
    "attendance": 85,
    "study_hours": 3,
    "previous_marks": 78,
    "assignment_score": 80
}])

prediction = model.predict(new_student)

print("Predicted Performance:", prediction[0])

# Save trained model
joblib.dump(model, "student_model.pkl")

print("Model Saved Successfully!")