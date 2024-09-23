import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Sample data
control_group = np.random.normal(loc=5, scale=1, size=100)
treatment_group = np.random.normal(loc=6, scale=1, size=100)

# T-test
t_statistic, p_value = stats.ttest_ind(treatment_group, control_group)

# Visualization
plt.boxplot([control_group, treatment_group], labels=['Placebo', 'Treatment'])
plt.ylabel('Outcome Measurement')
plt.title('Comparison of Treatment and Placebo Groups')
plt.annotate(f'p-value: {p_value:.4f}', xy=(1.5, np.max(np.concatenate([control_group, treatment_group]))), 
             ha='center', fontsize=12, color='red')
plt.show()

# Print the t-statistic and p-value
print(f'T-statistic: {t_statistic}, P-value: {p_value}')
