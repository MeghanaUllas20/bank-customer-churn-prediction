import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load data
df = pd.read_csv("Churn_Modelling.csv")

# Drop unused columns
df = df.drop(["RowNumber", "CustomerId", "Surname"], axis=1)

# Encode categories
geo_enc = LabelEncoder()
gender_enc = LabelEncoder()

df["Geography"] = geo_enc.fit_transform(df["Geography"])
df["Gender"] = gender_enc.fit_transform(df["Gender"])

# Split
X = df.drop("Exited", axis=1)
y = df["Exited"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Save everything
joblib.dump(model, "model.pkl")
joblib.dump(geo_enc, "geo_encoder.pkl")
joblib.dump(gender_enc, "gender_encoder.pkl")

print("✅ Model trained and saved!")
