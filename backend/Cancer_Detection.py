# Import necessary libraries 
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import joblib  # To save and also load the model
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc

# Load the dataset
try:
    data_path = r'e:/FinalML/The_Cancer_data_1500_V2.csv'
    data = pd.read_csv(data_path)
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print(f"Error: File not found at {data_path}. Please check the file path.")
    exit()

# Handle missing values (numeric columns only)
data.fillna(data.select_dtypes(include=[np.number]).mean(), inplace=True)

# Prepare the data for training
if 'Diagnosis' not in data.columns:
    print("Error: 'Diagnosis' column not found in the dataset.")
    exit()

X = data.drop('Diagnosis', axis=1)  # Features
y = data['Diagnosis']  # Target variable

# Ensure the dataset is not empty or invalid
if X.empty or y.empty:
    print("Error: Features or target variable is empty.")
    exit()

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the RFC's Value with default parameters
model = RandomForestClassifier(random_state=42, n_estimators=100, max_depth=None)

# Train the model
model.fit(X_train, y_train)

# Saved Tr-dAta for the future use
model_path = 'Cancer_Detection.pkl'
joblib.dump(model, model_path)
print(f"Model saved at {model_path}.")

# Cross-validation on the training set
scores = cross_val_score(model, X_train, y_train, cv=5)
print("Cross-validation scores (training set):", scores)
print("Mean cross-validation score:", np.mean(scores))

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nAccuracy Score:")
print(accuracy_score(y_test, y_pred))

# Display the confusion matrix
print("\nConfusion Matrix:")
cm = confusion_matrix(y_test, y_pred)
print(f"""
[True Neg  False Pos]    [{cm[0][0]}    {cm[0][1]}]
[False Neg True Pos]     [{cm[1][0]}    {cm[1][1]}]
""")

# Plot ROC Curve
def plot_roc_curve(y_test, y_pred_proba):
    fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
    roc_auc = auc(fpr, tpr)
    
    plt.figure(figsize=(8, 6))
    plt.plot(fpr, tpr, 'b-', label=f'ROC (AUC = {roc_auc:.2f})')
    plt.plot([0, 1], [0, 1], 'r--')  # diagonal line
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    plt.legend(loc='lower right')
    plt.grid(True)
    plt.savefig('roc_curve.png')
    plt.close()

# Plot Feature Importance
def plot_feature_importance(model, feature_names):
    importances = model.feature_importances_
    # Sort features by importance
    feature_importance_pairs = list(zip(feature_names, importances))
    feature_importance_pairs.sort(key=lambda x: x[1], reverse=True)
    
    # Unzip the sorted pairs
    features, importance = zip(*feature_importance_pairs)
    
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(features)), importance)
    plt.xticks(range(len(features)), features, rotation=45, ha='right')
    plt.xlabel('Features')
    plt.ylabel('Importance')
    plt.title('Feature Importance in Cancer Detection')
    plt.tight_layout()
    plt.savefig('feature_importance.png')
    plt.close()

# A simple confusion matrix
def plot_confusion_matrix(cm):
    plt.figure(figsize=(8, 6))
    plt.imshow([[0,0],[0,0]], cmap='Greys', alpha=0.1)
    
    # Add numbers to cells
    plt.text(0, 0, str(cm[0][0]), ha='center', va='center', fontsize=16)
    plt.text(1, 0, str(cm[0][1]), ha='center', va='center', fontsize=16)
    plt.text(0, 1, str(cm[1][0]), ha='center', va='center', fontsize=16)
    plt.text(1, 1, str(cm[1][1]), ha='center', va='center', fontsize=16)
    
    # Add labels
    plt.title('Confusion Matrix')
    plt.ylabel('Actual')
    plt.xlabel('Predicted')
    
    # Add class labels
    plt.xticks([0, 1], ['No Cancer', 'Cancer'])
    plt.yticks([0, 1], ['No Cancer', 'Cancer'])
    
    plt.tight_layout()
    plt.savefig('confusion_matrix.png')
    plt.close()

# Generate the plots
print("\nGenerating plots...")

# ROC Curve
y_pred_proba = model.predict_proba(X_test)[:, 1]
plot_roc_curve(y_test, y_pred_proba)
print("ROC curve plot saved as 'roc_curve.png'")

# Feature Importance
feature_names = X.columns
plot_feature_importance(model, feature_names)
print("Feature importance plot saved as 'feature_importance.png'")

# SHowing nw the acual confusion matrix
print("\nGenerating confusion matrix plot...")
plot_confusion_matrix(cm)
print("Confusion matrix plot saved as 'confusion_matrix.png'")

# Function to make predictions based on user input
def predict_cancer(features):
    try:
        model = joblib.load(model_path)  # Load the trained model
        prediction = model.predict([features])
        return prediction[0]
    except Exception as e:
        print(f"Error loading or predicting with the model: {e}")
        return None

# Main function to run that in case  the prediction
if __name__ == "__main__":
    print("\nEnter the following details for prediction:")
    
    #user input
    try:
        age = float(input("Age: "))
        if age < 0:
            raise ValueError("Age must be positive.")
        gender = int(input("Gender (1 for male, 0 for female): "))
        if gender not in [0, 1]:
            raise ValueError("Invalid gender value.")
        bmi = float(input("BMI: "))
        if bmi <= 0:
            raise ValueError("BMI must be positive.")
        smoking = int(input("Smoking Status (1 for smoker, 0 for non-smoker): "))
        if smoking not in [0, 1]:
            raise ValueError("Invalid smoking status.")
        genetic_risk = int(input("Genetic Risk Level (0-2): "))
        if genetic_risk not in [0, 1, 2]:
            raise ValueError("Invalid genetic risk level.")
        physical_activity = float(input("Physical Activity (1-10): "))
        if not (1 <= physical_activity <= 10):
            raise ValueError("Physical activity must be between 1 and 10.")
        alcohol_intake = float(input("Alcohol Intake (1-5): "))
        if not (1 <= alcohol_intake <= 5):
            raise ValueError("Alcohol intake must be between 1 and 5.")
        cancer_history = int(input("Family Cancer History (1 for yes, 0 for no): "))
        if cancer_history not in [0, 1]:
            raise ValueError("Invalid family cancer history.")
    
        # Prepare the features for prediction
        features = [age, gender, bmi, smoking, genetic_risk, physical_activity, alcohol_intake, cancer_history]
        
        # Futher prediction
        result = predict_cancer(features)
        
        # Display the reslt
        if result is None:
            print("Prediction could not be made.")
        elif result == 1:
            print("Prediction: Cancer detected.")
        else:
            print("Prediction: No cancer detected.")
    except ValueError as e:
        print(f"Invalid input: {e}")
