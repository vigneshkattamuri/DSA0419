import pandas as pd
import numpy as np
from scipy import stats

# Load the dataset
data = pd.read_csv('customer_reviews.csv')

# View the first few rows of the data to understand its structure
print(data.head())

# Assuming the CSV has the following columns: 'category', 'rating'
# Filter data for a specific product category (e.g., "Electronics")
category = input("Enter the product category you want to analyze: ")
filtered_data = data[data['category'] == category]

# Get the 'rating' column from the filtered data
ratings = filtered_data['rating']

# Calculate the sample mean and standard error of the mean
mean_rating = np.mean(ratings)
std_err = stats.sem(ratings)  # Standard error of the mean

# Set the confidence level (e.g., 95%)
confidence_level = 0.95
degrees_of_freedom = len(ratings) - 1
t_value = stats.t.ppf((1 + confidence_level) / 2, degrees_of_freedom)

# Calculate the margin of error
margin_of_error = t_value * std_err

# Calculate the confidence interval
ci_lower = mean_rating - margin_of_error
ci_upper = mean_rating + margin_of_error

# Output the results
print(f"\nFor the product category '{category}':")
print(f"Sample Mean Rating: {mean_rating:.4f}")
print(f"{int(confidence_level * 100)}% Confidence Interval: ({ci_lower:.4f}, {ci_upper:.4f})")
print(f"Margin of Error: {margin_of_error:.4f}")

# Insight based on confidence interval
if ci_lower >= 4:
    print(f"\nThe customers are generally very satisfied with products in the '{category}' category.")
elif ci_lower >= 3:
    print(f"\nThe customers are moderately satisfied with products in the '{category}' category.")
else:
    print(f"\nThe customer satisfaction for products in the '{category}' category is relatively low.")
