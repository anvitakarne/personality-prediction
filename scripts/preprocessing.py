import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download necessary NLP tools
nltk.download("stopwords")
nltk.download("punkt")

def preprocess_text(text):
    """Clean and preprocess text"""
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word.isalpha()]
    tokens = [word for word in tokens if word not in stopwords.words("english")]
    return " ".join(tokens)

# Load dataset
df = pd.read_csv("../data/mbti_sample.csv")
df["processed_text"] = df["text"].apply(preprocess_text)

# Save cleaned dataset
df.to_csv("../data/mbti_preprocessed.csv", index=False)
print("Preprocessing Complete. File saved to data/mbti_preprocessed.csv")

