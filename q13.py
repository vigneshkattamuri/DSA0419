from collections import Counter
import string

try:
    # Step 1: Read the text document
    with open('sample_text.txt', 'r') as file:
        text = file.read()

    # Debug: Print first 100 characters of the text
    print("Sample text:", text[:100])

    # Step 2: Process the text
    # Convert to lowercase to ensure case insensitivity
    text = text.lower()

    # Remove punctuation using str.translate and string.punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Split the text into words
    words = text.split()

    # Debug: Print the first 10 words
    print("First 10 words:", words[:10])

    # Step 3: Calculate the frequency distribution using Counter
    word_counts = Counter(words)

    # Debug: Print a sample of word counts
    print("Sample word counts:", dict(list(word_counts.items())[:10]))

    # Step 4: Display the frequency distribution
    for word, count in word_counts.items():
        print(f"'{word}': {count}")

except Exception as e:
    print("An error occurred:", e)


