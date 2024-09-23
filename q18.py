import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

# Data from the table in the image
data = {
    'age': [23, 23, 27, 27, 27, 39, 41, 47, 49, 50, 52, 54, 54, 56, 57, 58, 58, 60, 61],
    '%fat': [9.5, 26.5, 7.8, 17.8, 31.4, 25.9, 27.4, 27.2, 31.2, 34.6, 42.5, 28.8, 33.4, 30.2, 34.1, 32.9, 41.2, 41.2, 35.7]
}

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Calculate mean, median, and standard deviation
age_mean = df['age'].mean()
age_median = df['age'].median()
age_std = df['age'].std()

fat_mean = df['%fat'].mean()
fat_median = df['%fat'].median()
fat_std = df['%fat'].std()

print(f"Age - Mean: {age_mean}, Median: {age_median}, Standard Deviation: {age_std}")
print(f"%Fat - Mean: {fat_mean}, Median: {fat_median}, Standard Deviation: {fat_std}")

# Boxplot for age and %fat
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.boxplot(y=df['age'])
plt.title('Boxplot of Age')

plt.subplot(1, 2, 2)
sns.boxplot(y=df['%fat'])
plt.title('Boxplot of %Fat')
plt.tight_layout()
plt.show()

# Scatter plot of Age vs %Fat
plt.figure(figsize=(6, 6))
plt.scatter(df['age'], df['%fat'])
plt.title('Scatter Plot of Age vs %Fat')
plt.xlabel('Age')
plt.ylabel('%Fat')
plt.show()

# Q-Q plots for Age and %Fat
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
stats.probplot(df['age'], dist="norm", plot=plt)
plt.title('Q-Q Plot for Age')

plt.subplot(1, 2, 2)
stats.probplot(df['%fat'], dist="norm", plot=plt)
plt.title('Q-Q Plot for %Fat')

plt.tight_layout()
plt.show()
