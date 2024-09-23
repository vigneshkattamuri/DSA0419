import pandas as pd
from collections import Counter

# Sample DataFrame (replace this with actual data loading step)
data = {
    'post_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'likes': [10, 23, 10, 45, 67, 45, 23, 12, 10, 67]
}

df = pd.DataFrame(data)

# Step 1: Extract the 'likes' column
likes = df['likes']

# Step 2: Calculate the frequency distribution of likes using Counter
like_counts = Counter(likes)

# Step 3: Display the frequency distribution
print("Frequency Distribution of Likes:")
for like_count, frequency in like_counts.items():
    print(f"{like_count} likes: {frequency} posts")
