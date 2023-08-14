import numpy as np
student_scores = np.array([
    [90, 85, 78, 92],
    [78, 89, 92, 88],
    [90, 85, 78, 92],
    [78, 89, 92, 88],
])
average_scores = np.mean(student_scores, axis=0)
highest_average_subject= np.argmax(average_scores)
subjects = ['Math', 'Science', 'English','History']
for i, subject in enumerate(subjects):
    print(f"Average score in {subject}: {average_scores[i]}")
print(f"The subject with the highest average score is: {subjects[highest_average_subject]}")
