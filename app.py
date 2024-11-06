# app.py
import streamlit as st
import os
from src.data_loader import DataLoader
from src.sentiment_analyzer import SentimentAnalyzer

def main():
    st.title("Sentiment Analysis Chatbot")
    st.write("Analyze product reviews for sentiment.")

    # Input for OpenAI API key
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    if not OPENAI_API_KEY:
        OPENAI_API_KEY = st.text_input("Enter your OpenAI API Key", type="password")

    if not OPENAI_API_KEY:
        st.warning("Please enter your OpenAI API key.")
        st.stop()

    # Initialize the data loader and sentiment analyzer
    data_loader = DataLoader(file_path='data/Reviews.csv')
    sentiment_analyzer = SentimentAnalyzer(api_key=OPENAI_API_KEY)

    # Input for product ID
    product_id = st.text_input("Enter Product ID to analyze")

    if st.button("Analyze"):
        if not product_id:
            st.warning("Please enter a Product ID.")
            st.stop()

        with st.spinner(f"Analyzing reviews for {product_id}..."):
            reviews = data_loader.filter_reviews(product_id)

            if reviews.empty:
                st.error("No reviews found for this product.")
                st.info("Try using a different Product ID.")
                st.stop()
            st.error(reviews)
            analysis = sentiment_analyzer.analyze_reviews(reviews)
            if analysis:
                st.success(f"Analysis complete for Product ID: {product_id}")
                display_analysis(analysis)
            else:
                st.error("An error occurred during analysis.")

def display_analysis(analysis):
    st.header(f"Product ID: {analysis.get('Product_ID', 'N/A')}")
    st.subheader(f"Total Reviews Analyzed: {analysis.get('total_reviews', 'N/A')}")
    st.subheader(f"Average Rating: {analysis.get('average_rating', 'N/A'):.2f} / 5")

    top_sentiments = analysis.get('top_sentiments', [])
    for idx, sentiment in enumerate(top_sentiments, 1):
        st.write(f"### {idx}. {sentiment.get('category', 'N/A')}")
        st.write(f"**Sentiment:** {sentiment.get('sentiment', 'N/A')} ({sentiment.get('confidence', 'N/A')}% confidence)")
        st.write(f"**Common Themes:** {', '.join(sentiment.get('themes', []) or [])}")
        st.write(f"**Example Review:** {sentiment.get('example_review', 'N/A')}")

if __name__ == "__main__":
    main()
