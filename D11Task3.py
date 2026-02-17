import matplotlib.pyplot as plt

# Data
study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
scores = [50, 55, 65, 70, 75, 85, 90, 95]

# Create Scatter Plot
plt.scatter(study_hours, scores)

# Labels and Title
plt.xlabel("Study Hours")
plt.ylabel("Exam Scores")
plt.title("Study Hours vs Exam Scores")

# Show grid (optional but helpful)
plt.grid(True)

# Display the plot
plt.show()
