import numpy as np
from scipy import stats

# Example data: Conversion rates for design A and design B
conversion_rates_A = [0.05, 0.06, 0.04, 0.07, 0.06, 0.05, 0.07, 0.05, 0.06, 0.04]
conversion_rates_B = [0.07, 0.08, 0.06, 0.07, 0.09, 0.08, 0.07, 0.08, 0.09, 0.07]

# Perform a two-sample t-test (assuming unequal variances)
t_stat, p_value = stats.ttest_ind(conversion_rates_A, conversion_rates_B, equal_var=False)

# Output the t-statistic and p-value
print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {p_value:.4f}")

# Significance level
alpha = 0.05

# Interpretation of the result
if p_value < alpha:
    print("Reject the null hypothesis. There is a statistically significant difference in the mean conversion rates between design A and design B.")
else:
    print("Fail to reject the null hypothesis. There is no statistically significant difference in the mean conversion rates between design A and design B.")
