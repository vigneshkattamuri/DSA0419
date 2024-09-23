  import pandas as pd
from collections import Counter

# Sample DataFrame (replace this with your actual data loading step)
data = {
    'customer_id': [1, 2, 3, 4, 5, 6],
    'purchase_date': ['2024-08-01', '2024-08-05', '2024-08-07', '2024-08-10', '2024-08-12', '2024-08-20'],
    'age': [25, 34, 29, 40, 30, 22]
}

df = pd.DataFrame(data)

# Step 1: Extract the age column
ages = df['age']

# Step 2: Calculate the frequency distribution using Counter
age_counts = Counter(ages)

# Step 3: Display the frequency distribution
print("Frequency Distribution of Ages:")
for age, count in age_counts.items():
    print(f"Age {age}: {count} customers")
