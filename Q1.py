import numpy as np
np.random.seed(42)
student_scores = np.random.randint(0, 101, size=(32, 4))
average_scores = np.mean(student_scores, axis=0)
highest_avg_index = np.argmax(average_scores)
subjects = ['Math', 'Science', 'English', 'History']
highest_avg_subject = subjects[highest_avg_index]
print("Average Scores for Each Subject:")
for subject, avg_score in zip(subjects, average_scores):
    print(f"{subject}: {avg_score:.2f}")
print(f"\nSubject with the Highest Average Score: {highest_avg_subject} ({average_scores[highest_avg_index]:.2f})")
lowest_avg_index = np.argmin(average_scores)
lowest_avg_subject = subjects[lowest_avg_index]
print(f"Subject with the Lowest Average Score: {lowest_avg_subject} ({average_scores[lowest_avg_index]:.2f})")
