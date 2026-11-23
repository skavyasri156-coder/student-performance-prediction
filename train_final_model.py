import pandas as pd
import joblib
from sklearn.tree import DecisionTreeClassifier

# 1. Load the dataset
df = pd.read_csv("dataset/students_big.csv")

X = df[["attendance", "study_hours", "previous_marks", "assignment_score"]]
y = df["performance"]

# 2. Train the final model on ALL 60 records
model = DecisionTreeClassifier(max_depth=5, random_state=42)
model.fit(X, y)

# 3. Save it
joblib.dump(model, "student_model_final.pkl")

print("Final model trained on", len(df), "records")
print("Saved as student_model_final.pkl")
print("Classes:", list(model.classes_))