import numpy as np
import pandas as pd

# This makes the random numbers the same every time we run
np.random.seed(42)

n = 60  # number of students

attendance = np.random.randint(50, 100, n)         # 50 to 99 percent
study_hours = np.random.randint(1, 9, n)           # 1 to 8 hours per day
previous_marks = np.random.randint(35, 100, n)     # 35 to 99 marks
assignment_score = np.random.randint(30, 100, n)   # 30 to 99 marks

# A simple score to decide performance (with a little random noise)
score = (
    0.25 * attendance
    + 4 * study_hours
    + 0.30 * previous_marks
    + 0.20 * assignment_score
    + np.random.randint(-5, 6, n)
)

performance = []
for s in score:
    if s >= 80:
        performance.append("Good")
    elif s >= 65:
        performance.append("Average")
    else:
        performance.append("Poor")

df = pd.DataFrame({
    "attendance": attendance,
    "study_hours": study_hours,
    "previous_marks": previous_marks,
    "assignment_score": assignment_score,
    "performance": performance,
})

df.to_csv("dataset/students_big.csv", index=False)

print("New dataset saved: dataset/students_big.csv")
print(df.head(10))
print()
print("Count of each performance class:")
print(df["performance"].value_counts())