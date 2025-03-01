import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Embedding, Dropout

# Load preprocessed data
df = pd.read_csv("../data/mbti_preprocessed.csv")

# Define model
model = Sequential([
    Embedding(input_dim=10000, output_dim=128, input_length=100),
    LSTM(128, return_sequences=True),
    Dropout(0.5),
    Dense(16, activation="softmax")
])

# Compile & train
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
model.fit(df["processed_text"], df["personality"], epochs=5)

# Save model
model.save("../models/personality_model.h5")
print("Model saved to models/personality_model.h5")

