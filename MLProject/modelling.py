import os
import mlflow
import mlflow.sklearn
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# Path dataset
DATA_PATH = "namadataset_preprocessing/diabetes_preprocessing.csv"

# Load dataset
data = pd.read_csv(DATA_PATH)

# Pisahkan fitur dan target
# GANTI 'target' sesuai nama kolom label di dataset kamu
X = data.drop(columns=["Outcome"])
y = data["Outcome"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Mulai MLflow run
with mlflow.start_run():
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    # Logging parameter dan metric
    mlflow.log_param("model_type", "RandomForestClassifier")
    mlflow.log_param("test_size", 0.2)
    mlflow.log_metric("accuracy", accuracy)

    # Simpan model lokal
    os.makedirs("artifacts", exist_ok=True)
    joblib.dump(model, "artifacts/model.joblib")

    # Log artifact ke MLflow
    mlflow.log_artifact("artifacts/model.joblib")
    mlflow.sklearn.log_model(model, "model")

    print(f"Accuracy: {accuracy}")