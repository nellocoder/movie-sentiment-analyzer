# movie-sentiment-analyzer
It uses sentimental analysis to analyze and predict reviews on movies. 
# 🍿 AI Movie Critic (Sentiment Analysis)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Library](https://img.shields.io/badge/Library-Scikit--Learn-orange)
![Status](https://img.shields.io/badge/Status-Deployed-success)

## 📌 Project Overview
This project is a **Natural Language Processing (NLP)** application that analyzes movie reviews and automatically classifies them as **Positive** or **Negative**.

The system is built using Python and Scikit-Learn, leveraging **TF-IDF Vectorization** to translate unstructured text into numerical features and a **Multinomial Naive Bayes** classifier to predict sentiment with high accuracy.

**🔗 Live Demo:** [INSERT YOUR STREAMLIT LINK HERE]

---

## 🧠 Model Performance
The model was trained on a balanced dataset of 10,000 IMDB movie reviews.

| Metric | Score | Interpretation |
| :--- | :--- | :--- |
| **Accuracy** | **85.20%** | The model correctly identifies sentiment 85% of the time, which is ~35% better than random guessing. |
| **Precision** | **0.85** | The model is highly reliable; when it says a review is positive, it is usually right. |
| **Recall** | **0.85** | The model rarely "misses" true positive or negative reviews. |

### 🧪 Real-World "Stress Test"
To verify the model isn't just memorizing keywords (like "bad" or "good"), we tested it on implicit sentiment.

* **Test Sentence:** *"I would rather watch paint dry than watch this again."*
* **Prediction:** **NEGATIVE (Confidence: 69.80%)**
* **Insight:** The model successfully identified the
