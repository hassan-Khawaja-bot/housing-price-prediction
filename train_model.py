import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score

# Load dataset
df = pd.read_csv("data/housing.csv")

# Handle missing values
df["total_bedrooms"].fillna(df["total_bedrooms"].median(), inplace=True)

# Feature selection
X = df.drop("median_house_value", axis=1)
y = df["median_house_value"]

# Convert categorical column
X = pd.get_dummies(X, columns=["ocean_proximity"], drop_first=True)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Pipeline (Scaling + Model)
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LinearRegression())
])

# Train model
pipeline.fit(X_train, y_train)

# Evaluate
y_pred = pipeline.predict(X_test)
print("R2 Score:", r2_score(y_test, y_pred))

# Save model
joblib.dump(pipeline, "model/model.pkl")
print("Model saved successfully!")
