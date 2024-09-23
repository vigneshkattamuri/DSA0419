import string
from collections import Counter

# Sample list of customer reviews (can be replaced with dataset loading)
reviews = [
    "The product is great, I love it!",
    "Great quality, but delivery was slow.",
    "Love this product! Will recommend it to my friends.",
    "Terrible experience, the product broke after one use.",
    "Great product, but could be cheaper."
]

def preprocess_review(review):
    """
    Function to preprocess the review text: remove punctuation, convert to lowercase.
    """
    # Remove punctuation
    review = review.translate(str.maketrans('', '', string.punctuation))
    # Convert to lowercase
    review = review.lower()
    return review

def calculate_word_frequency(reviews):
    """
    Function to calculate word frequency distribution from a list of reviews.
    """
    all_words = []
    
    # Preprocess each review and split into words
    for review in reviews:
        processed_review = preprocess_review(review)
        words = processed_review.split()
        all_words.extend(words)
    
    # Calculate word frequency using Counter
    word_freq = Counter(all_words)
    
    return word_freq

# Calculate word frequency
word_frequency = calculate_word_frequency(reviews)

# Print the word frequency distribution
print("Word Frequency Distribution:")
for word, freq in word_frequency.items():
    print(f"{word}: {freq}")
