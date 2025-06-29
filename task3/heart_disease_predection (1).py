# -*- coding: utf-8 -*-
"""heart disease predection.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jpGQDy9_3pXR9qt6Py3UYMZkfE6cPAI5
"""

from google.colab import files
uploaded = files.upload()  # Manually select the downloaded file.

import pandas as pd

# Load and display first 5 rows + columns
df = pd.read_csv('heart_disease_uci.csv')
print(df.head())  # Shows first 5 rows and all columns

# Separate numeric and non-numeric columns
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
categorical_cols = df.select_dtypes(exclude=['int64', 'float64']).columns

# Calculate missing values
missing_values = df.isnull().sum()

# Fill missing values: median for numeric, mode for categorical
if missing_values.any():
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
    df[categorical_cols] = df[categorical_cols].fillna(df[categorical_cols].mode().iloc[0])
    print("Missing values handled (numeric: median, categorical: mode).")
else:
    print("No missing values found.")

# Verify
print("\nMissing values after handling:")
print(df.isnull().sum())

"""## **Exploratory data analysis**
a type of analysis which contain ultiple types of small analysis through which model can easily analyze many relations between difference cols rows and values
"""

# ======================
# 1. IMPORT LIBRARIES
# ======================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ======================
# 2. LOAD DATASET
# ======================
df = pd.read_csv('heart_disease_uci.csv')

# ======================
# 3. BASIC DATA INSPECTION
# ======================
print("\n=== Dataset Shape ===")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

print("\n=== First 5 Rows ===")
print(df.head())

print("\n=== Data Types ===")
print(df.dtypes)

# ======================
# 4. STATISTICAL SUMMARY
# ======================
print("\n=== Numerical Features Summary ===")
print(df.describe())

print("\n=== Categorical Features Summary ===")
cat_cols = df.select_dtypes(include=['object']).columns
if len(cat_cols) > 0:
    print(df[cat_cols].describe())
else:
    print("No categorical columns found")

# ======================
# 5. DISTRIBUTION ANALYSIS
# ======================
print("\n=== Plotting Numerical Distributions ===")
num_cols = df.select_dtypes(include=['int64', 'float64']).columns
plt.figure(figsize=(15, 10))
for i, col in enumerate(num_cols[:12]):  # Plot first 12 numerical columns
    plt.subplot(3, 4, i+1)
    sns.histplot(df[col], kde=True)
    plt.title(f'Distribution of {col}')
plt.tight_layout()
plt.show()

# ======================
# 6. CATEGORICAL ANALYSIS (FIXED)
# ======================
if len(cat_cols) > 0:
    print("\n=== Plotting Categorical Counts ===")
    plt.figure(figsize=(15, 5))

    # Only plot if <=5 categorical columns to avoid overcrowding
    cols_to_plot = cat_cols[:5]  # Limits to first 5 categorical columns

    for i, col in enumerate(cols_to_plot):
        plt.subplot(1, len(cols_to_plot), i+1)
        sns.countplot(data=df, x=col, palette='viridis')  # Added color palette
        plt.title(f'Distribution of {col}', fontsize=12)  # Better title
        plt.xticks(rotation=45)  # Rotate x-labels if needed

    plt.tight_layout()
    plt.show()
else:
    print("No categorical columns found for analysis.")

# ======================
# 7. OUTLIER DETECTION
# ======================
print("\n=== Checking for Outliers ===")
plt.figure(figsize=(15, 5))
sns.boxplot(data=df[num_cols[:5]])  # First 5 numerical features
plt.title('Boxplot of Numerical Features')
plt.xticks(rotation=45)
plt.show()

# ======================
# 8. CORRELATION ANALYSIS
# ======================

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder  # <-- THIS WAS MISSING

# Encode categorical data
df_encoded = df.copy()
for col in df.select_dtypes(include=['object']).columns:
    df_encoded[col] = LabelEncoder().fit_transform(df[col])

# Generate heatmap
plt.figure(figsize=(12, 8))
corr_matrix = df_encoded.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, fmt='.2f')  # Added fmt for 2 decimal places
plt.title('Feature Correlations')
plt.tight_layout()  # Prevents label cutoff
plt.show()

# ======================
# 9. num ANALYSIS
# ======================
if 'num' in df.columns:
    print("\n=== num Variable Analysis ===")
    print("\nClass Distribution:")
    print(df['num'].value_counts())

    plt.figure(figsize=(12, 6))
    for i, col in enumerate(num_cols[:6]):  # Compare first 6 features vs target
        plt.subplot(2, 3, i+1)
        sns.boxplot(data=df, x='num', y=col)
        plt.title(f'{col} by num')
    plt.tight_layout()
    plt.show()

"""# **Step 1: Prepare the Data**"""

#Encode Categorical Features
from sklearn.preprocessing import LabelEncoder

# Encode categorical columns (if any)
df_encoded = df.copy()
for col in df.select_dtypes(include=['object']).columns:
    df_encoded[col] = LabelEncoder().fit_transform(df[col])

#B. Define Features (X) and Target (y)

X = df_encoded.drop(columns=['num'])  # Features (all columns except num)
y = df_encoded['num']                # num (0: no disease, 1+: disease)

# For binary classification, merge severity levels (optional):
y_binary = (y > 0).astype(int)  # Converts 1-4 → 1 (disease)

"""# Step 2: Split Data into Train/Test Sets"""

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y_binary, test_size=0.3, random_state=42
)

"""# **Step 3: Train Models**"""

# Option B: Decision Tree

from sklearn.tree import DecisionTreeClassifier

model_dt = DecisionTreeClassifier(max_depth=3, random_state=42)
model_dt.fit(X_train, y_train)

"""# **Step 4: Evaluate Models**"""

#accuracy score
from sklearn.metrics import accuracy_score


y_pred_dt = model_dt.predict(X_test)
print("Decision Tree Accuracy:", accuracy_score(y_test, y_pred_dt))

"""# **Confusion matrix**"""

from sklearn.metrics import confusion_matrix


print("DT Confusion Matrix:\n", confusion_matrix(y_test, y_pred_dt))

"""# **ROC Curve (Advanced)**"""

from sklearn.metrics import RocCurveDisplay

RocCurveDisplay.from_estimator(model_dt, X_test, y_test)
plt.title('ROC Curve (Logistic Regression)')
plt.show()

importance_df = pd.DataFrame({
    'Feature': X_train.columns,
    'Importance': model_dt.feature_importances_
}).sort_values('Importance', ascending=False)

print("\nDecision Tree Feature Importance:")
print(importance_df.head(10))