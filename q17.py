import pandas as pd
import string
from collections import Counter
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Load the dataset from CSV file (assuming the file is named 'data.csv' and has a column 'feedback')
df = pd.read_csv('data.csv')

# Extract the 'feedback' column and drop any missing values
feedbacks = df['feedback'].dropna()

# Function to preprocess text: lowercase, remove punctuation, and remove stopwords
def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Tokenize the text
    tokens = word_tokenize(text)
    # Remove stopwords (common words that don't carry significant meaning)
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    return tokens

# Initialize an empty list to store all tokens
all_words = []

# Process each feedback entry
for feedback in feedbacks:
    tokens = preprocess_text(feedback)
    all_words.extend(tokens)

# Calculate word frequency using Counter
word_freq = Counter(all_words)

# Ask the user to input the number of top frequent words (N)
N = int(input("Enter the number of top frequent words to display: "))

# Get the top N most frequent words
most_common_words = word_freq.most_common(N)

# Display the top N words and their frequencies
print(f"\nTop {N} most frequent words:")
for word, freq in most_common_words:
    print(f"{word}: {freq}")

# Plot a bar graph of the top N most frequent words
words, counts = zip(*most_common_words)  # Unzip the word-frequency pairs
plt.figure(figsize=(10, 6))
plt.bar(words, counts, color='blue')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title(f'Top {N} Most Frequent Words in Customer Feedback')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

