import numpy as np
import pandas as pd
import scipy.stats as stats

# Function to calculate the confidence interval
def confidence_interval(sample, confidence_level):
    n = len(sample)
    mean = np.mean(sample)
    std_err = stats.sem(sample)  # Standard error of the mean
    t_value = stats.t.ppf((1 + confidence_level) / 2, n - 1)  # t critical value
    margin_of_error = t_value * std_err
    
    return mean, mean - margin_of_error, mean + margin_of_error, margin_of_error

# Load the dataset
data = pd.read_csv('rare_elements.csv')

# Get the user inputs
sample_size = int(input("Enter the sample size: "))
confidence_level = float(input("Enter the confidence level (e.g., 0.95 for 95%): "))
precision = float(input("Enter the desired level of precision (half-width of the CI): "))

# Randomly sample from the dataset
sample = data.sample(n=sample_size, random_state=42)['concentration']

# Calculate the confidence interval
mean, ci_lower, ci_upper, margin_of_error = confidence_interval(sample, confidence_level)

# Display the results
print(f"\nSample Mean: {mean:.4f}")
print(f"{int(confidence_level * 100)}% Confidence Interval: ({ci_lower:.4f}, {ci_upper:.4f})")
print(f"Margin of Error (Precision): {margin_of_error:.4f}")

# Check if the desired precision is achieved
if margin_of_error <= precision:
    print(f"\nThe desired precision of ±{precision} has been achieved.")
else:
    print(f"\nThe desired precision of ±{precision} has NOT been achieved.")
    print(f"To achieve the desired precision, consider increasing the sample size.")
