
# Student marks

marks = [85, 90, 75, 60, 95]

# Function to calculate average

def calculate_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return average

# Display marks

print("STUDENT MARKS")

for mark in marks:
    print(mark)

# Display average

result = calculate_average(marks)

print("Average Marks:", result)
