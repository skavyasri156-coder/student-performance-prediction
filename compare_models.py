import pandas as pd
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# 1. Load the bigger dataset
df = pd.read_csv("dataset/students_big.csv")

X = df[["attendance", "study_hours", "previous_marks", "assignment_score"]]
y = df["performance"]

# 2. 5-fold cross-validation (split data into 5 parts, test 5 times)
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

print("Average accuracy using 5-fold cross-validation")
print("-" * 50)

# 3. Try different depths for Decision Tree
for depth in [2, 3, 4, 5, 6]:
    model = DecisionTreeClassifier(max_depth=depth, random_state=42)
    scores = cross_val_score(model, X, y, cv=cv)
    print("Decision Tree, max_depth =", depth, ":", round(scores.mean() * 100, 2), "%")

# 4. Try Random Forest
rf = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
scores = cross_val_score(rf, X, y, cv=cv)
print("Random Forest (100 trees)     :", round(scores.mean() * 100, 2), "%")