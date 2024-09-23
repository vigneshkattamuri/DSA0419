import numpy as np
import scipy.stats as stats

# Data for the drug group
mean_drug = 12.4
std_drug = 5.2
n_drug = 25

# Data for the placebo group
mean_placebo = 8.6
std_placebo = 4.8
n_placebo = 25

# 95% confidence interval for both groups
confidence_level = 0.95
alpha = 1 - confidence_level

# t critical value (two-tailed t-distribution)
t_drug = stats.t.ppf(1 - alpha/2, df=n_drug - 1)
t_placebo = stats.t.ppf(1 - alpha/2, df=n_placebo - 1)

# Confidence interval calculation for drug group
margin_of_error_drug = t_drug * (std_drug / np.sqrt(n_drug))
ci_lower_drug = mean_drug - margin_of_error_drug
ci_upper_drug = mean_drug + margin_of_error_drug

# Confidence interval calculation for placebo group
margin_of_error_placebo = t_placebo * (std_placebo / np.sqrt(n_placebo))
ci_lower_placebo = mean_placebo - margin_of_error_placebo
ci_upper_placebo = mean_placebo + margin_of_error_placebo

print(f"95% CI for drug group: ({ci_lower_drug:.2f}, {ci_upper_drug:.2f})")
print(f"95% CI for placebo group: ({ci_lower_placebo:.2f}, {ci_upper_placebo:.2f})")
