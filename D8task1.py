import numpy as np
scores = np.random.randint(50, 101, size=(5, 3))
subject_means = scores.mean(axis=0)
centered_scores = scores - subject_means
print("Original Scores (Students x Subjects):\n")
print(scores)
print("\nMean Score per Subject:\n")
print(subject_means)
print("\nCentered Scores (After Broadcasting):\n")
print(centered_scores)
