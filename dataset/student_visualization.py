import pandas as pd
import matplotlib.pyplot as plt

# Read student dataset
data = pd.read_csv("dataset/students.csv")

# Count performance categories
performance_count = data["performance"].value_counts()

# Create pie chart
plt.pie(
    performance_count,
    labels=performance_count.index,
    autopct="%1.1f%%"
)

# Add title
plt.title("Student Performance Distribution")

# Display chart
plt.show()