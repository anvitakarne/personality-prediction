from tensorflow.keras.models import load_model
import pandas as pd

# Load model & test data
model = load_model("../models/personality_model.h5")
test_df = pd.read_csv("../data/mbti_test.csv")

# Evaluate model
results = model.evaluate(test_df["processed_text"], test_df["personality"])
print(f"Test Accuracy: {results[1]:.4f}")

