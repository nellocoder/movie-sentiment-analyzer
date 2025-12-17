import streamlit as st
import joblib

# 1. LOAD THE SAVED MODELS
model = joblib.load('sentiment_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

# 2. APP INTERFACE
st.title("🍿 AI Movie Critic")
st.write("Enter a movie review below, and the AI will determine if it is **Positive** or **Negative**.")

# Text Input Box
user_text = st.text_area("Type your review here:", height=150)

if st.button("Analyze Sentiment"):
    if user_text:
        # 3. TRANSFORM INPUT (Text -> Numbers)
        text_vec = vectorizer.transform([user_text])
        
        # 4. PREDICT
        prediction = model.predict(text_vec)
        probability = model.predict_proba(text_vec)
        
        # Get confidence score (max probability)
        confidence = probability.max()
        sentiment = "POSITIVE" if prediction[0] == 'positive' else "NEGATIVE"
        
        # 5. DISPLAY RESULT
        st.write("---")
        st.subheader("The Verdict:")
        
        if sentiment == "POSITIVE":
            st.success(f"😃 **POSITIVE REVIEW** (Confidence: {confidence:.2%})")
            st.balloons()
        else:
            st.error(f"😡 **NEGATIVE REVIEW** (Confidence: {confidence:.2%})")
    else:

        st.warning("Please type a review first!")
