import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

# Sample dataset (replace with your actual data)
data = {
    'symptom1': [0, 1, 0, 1, 0],
    'symptom2': [1, 0, 0, 1, 1],
    'symptom3': [0, 1, 1, 0, 1],
    'condition': [0, 1, 0, 1, 1]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Features and labels
X = df[['symptom1', 'symptom2', 'symptom3']]
y = df['condition']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the feature values
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train the KNN classifier
k = 3  # Default value for k; this can be changed based on user input
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train, y_train)

# Function to make predictions for a new patient
def predict_condition(features, k):
    features = np.array(features).reshape(1, -1)  # Reshape for a single sample
    features_scaled = scaler.transform(features)  # Scale features
    prediction = knn.predict(features_scaled)
    return prediction[0]

# User input for features and k
user_features = []
print("Enter the features for the new patient (symptom1, symptom2, symptom3):")
for i in range(3):
    feature_value = float(input(f"Feature {i+1}: "))
    user_features.append(feature_value)

k_value = int(input("Enter the value of k (number of neighbors): "))

# Make prediction
result = predict_condition(user_features, k_value)

# Output result
if result == 1:
    print("The patient is predicted to have the medical condition.")
else:
    print("The patient is predicted not to have the medical condition.")
