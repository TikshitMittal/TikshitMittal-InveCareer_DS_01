import pandas as pd
import numpy as np


# Set the seed for reproducibility
np.random.seed(42)

# Generate a hypothetical dataset
n_students = 200
data = {
    'Student ID': np.arange(1, n_students + 1),
    'Exam Score': np.random.randint(50, 101, n_students),
    'Gender': np.random.choice(['Male', 'Female'], n_students),
    'Age': np.random.randint(15, 20, n_students),
    'Study Time per Week': np.random.randint(1, 20, n_students),
    'Parental Education Level': np.random.choice(['High School', 'Associate\'s Degree', 'Bachelor\'s Degree', 'Master\'s Degree'], n_students),
    'Attendance Rate': np.random.randint(60, 101, n_students)
}

# Create a DataFrame
df = pd.DataFrame(data)

# Show the first few rows of the DataFrame
df.head()


# Plot the distribution of exam scores
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))
sns.histplot(df['Exam Score'], bins=10, kde=True)
plt.title('Distribution of Exam Scores')
plt.xlabel('Exam Score')
plt.ylabel('Frequency')
plt.show()

# Scatter plot: Exam Score vs. Study Time per Week
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Study Time per Week', y='Exam Score', data=df)
plt.title('Exam Score vs. Study Time per Week')
plt.xlabel('Study Time per Week (hours)')
plt.ylabel('Exam Score')
plt.show()

# Calculate correlation coefficient between Exam Score and Study Time per Week
correlation_study_time = df['Exam Score'].corr(df['Study Time per Week'])
correlation_study_time

# Scatter plot: Exam Score vs Age
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Age', y='Exam Score', data=df)
plt.title('Exam Score vs. Age')
plt.xlabel('Age')
plt.ylabel('Exam Score')
plt.show()

# Calculate correlation coefficient between Exam Score and Age
correlation_age = df['Exam Score'].corr(df['Age'])
correlation_age


# Scatter plot: Exam Score vs Attendance Rate
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Attendance Rate', y='Exam Score', data=df)
plt.title('Exam Score vs. Attendance Rate')
plt.xlabel('Attendance Rate')
plt.ylabel('Exam Score')
plt.show()

# Calculate correlation coefficient between Exam Score and Attendance Rate
correlation_Attendance_Rate = df['Exam Score'].corr(df['Attendance Rate'])
correlation_Attendance_Rate

print(correlation_age)
print(correlation_Attendance_Rate)
print(correlation_study_time)

#Recommendations

#The histogram showed a relatively even distribution of exam scores, indicating no extreme skewness
#The correlation between exam score and study time was very low
#The correlation between exam score and attendance rate and with age were low too
#This suggests these parameter doesn't have a significant impact on exam score