import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Read dataset
data = pd.read_csv("dataset/students.csv")

# Select features
X = data[[
    "attendance",
    "study_hours",
    "previous_marks",
    "assignment_score"
]]

# Select target
y = data["performance"]

# Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.5,
    random_state=42,
    stratify=y
)

# Create model
model = DecisionTreeClassifier(random_state=42)

# Train model
model.fit(X_train, y_train)

# Predict test data
predictions = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, predictions)

print("Model Evaluation Results")
print("Accuracy:", accuracy * 100, "%")

# Display confusion matrix
matrix = confusion_matrix(
    y_test,
    predictions,
    labels=model.classes_
)

print("\nConfusion Matrix:")
print(matrix)