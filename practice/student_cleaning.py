import pandas as pd

# Read dataset
data = pd.read_csv("dataset/students.csv")

# Check missing values
print("MISSING VALUES BEFORE CLEANING")
print(data.isnull().sum())

# Fill missing numerical values with column average
data["attendance"] = data["attendance"].fillna(data["attendance"].mean())

data["study_hours"] = data["study_hours"].fillna(data["study_hours"].mean())

data["previous_marks"] = data["previous_marks"].fillna(data["previous_marks"].mean())

data["assignment_score"] = data["assignment_score"].fillna(data["assignment_score"].mean())

# Fill missing performance with most common category
data["performance"] = data["performance"].fillna(data["performance"].mode()[0])

# Check again
print("\nMISSING VALUES AFTER CLEANING")
print(data.isnull().sum())