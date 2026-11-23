import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# 1. Load the bigger dataset
df = pd.read_csv("dataset/students_big.csv")

# 2. Features (inputs) and target (output)
X = df[["attendance", "study_hours", "previous_marks", "assignment_score"]]
y = df["performance"]

# 3. Split into training (80%) and testing (20%) data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 4. Create and train the model
model = DecisionTreeClassifier(max_depth=4, random_state=42)
model.fit(X_train, y_train)

# 5. Check how good the model is
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print("Training records:", len(X_train))
print("Testing records :", len(X_test))
print("Accuracy        :", round(accuracy * 100, 2), "%")
print()
print("Confusion matrix:")
print(confusion_matrix(y_test, predictions, labels=["Poor", "Average", "Good"]))

# 6. Save the trained model
joblib.dump(model, "student_model_big.pkl")
print()
print("Model saved as student_model_big.pkl")