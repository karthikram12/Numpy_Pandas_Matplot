import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy import random

student_id = np.arange(1000, 1100)
subject_scores = random.randint(20, 100, size=(100, 3))

student_id_series = pd.Series(student_id, name='student_id')
subject_scores_df = pd.DataFrame(subject_scores, columns=['Maths', 'Physics', 'Chemistry'])

subject_scores_df['student_id'] = student_id_series
subject_scores_df = subject_scores_df.set_index('student_id')

subject_scores_df['total_marks'] = subject_scores_df.sum(axis=1)
subject_scores_df['average_marks'] = subject_scores_df['total_marks'] / 3

subject_scores_df['result'] = subject_scores_df['average_marks'].apply(lambda x: 'Pass' if x >=50 else 'Fail')
result_counts = subject_scores_df['result'].value_counts()

plt.subplot(3, 1, 1)
plt.hist(subject_scores_df['average_marks'], bins=10)
plt.xlabel('Average Marks')
plt.ylabel('Number of Students')

plt.subplot(3, 1, 2)
plt.bar(result_counts.index, result_counts.values, color =['red', 'green'])
plt.xlabel('Result')
plt.ylabel('Number of Students')

plt.subplot(3, 1, 3)
plt.scatter(subject_scores_df['Maths'], subject_scores_df['Physics'], color='red')
plt.xlabel('Maths')
plt.ylabel('Physics')
plt.show()