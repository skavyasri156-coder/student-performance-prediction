import pandas as pd
import numpy as np

# Read student dataset
data = pd.read_csv("dataset/students.csv")

# Display first 5 rows
print("STUDENT DATA")
print(data.head())

# Display dataset information
print("\nDATASET INFORMATION")
print(data.info())

# Calculate average marks
average = np.mean(data["previous_marks"])

print("\nAverage Previous Marks:", average)

# Find highest marks
highest = np.max(data["previous_marks"])

print("Highest Previous Marks:", highest)