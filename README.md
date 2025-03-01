# 🧠 Personality Prediction Using Deep Learning

🚀 This project explores **personality prediction** using **Machine Learning (ML) and Deep Learning (DL)** models.  
We compare traditional **Naïve Bayes** with advanced **LSTM, Bi-LSTM, Bi-LSTM + Attention, and DistilBERT** models on **MBTI personality type data**.

![Personality Distribution](figures/Personality_Distribution.png)

---

## 📌 **Project Overview**
- **🔍 Problem Statement:** Can we predict a person's MBTI personality type based on their textual data?
- **🧑‍💻 Models Used:**
  - ✅ **Naïve Bayes** (Baseline)
  - ✅ **LSTM** (Recurrent Neural Network)
  - ✅ **Bi-LSTM** (Bidirectional LSTM)
  - ✅ **Bi-LSTM + Attention** (Best Model - **96% Accuracy**)
  - ✅ **DistilBERT** (Transformer-based model)
- **📊 Dataset:** MBTI Personality Types Dataset (~8,000 samples)
- **⚡ Techniques Used:** NLP Preprocessing, Word Embeddings, Class Balancing (SMOTE)
- **🏆 Best Model:** **Bi-LSTM + Attention** achieved **96% accuracy** 🎯

---

## 🚀 **Installation & Setup**
To run this project locally:

1️⃣ **Clone the repository**  
```bash
git clone https://github.com/anvitakarne/personality-prediction.git
cd personality-prediction
